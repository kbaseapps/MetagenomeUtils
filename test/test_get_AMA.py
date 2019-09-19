import os  # noqa: F401
import shutil
import time
import unittest
import zipfile
from configparser import ConfigParser
from os import environ
from pprint import pprint  # noqa: F401
import json

from MetagenomeUtils.MetagenomeUtilsImpl import MetagenomeUtils
from MetagenomeUtils.MetagenomeUtilsServer import MethodContext
from MetagenomeUtils.Utils.MetagenomeFileUtils import MetagenomeFileUtils
from MetagenomeUtils.Utils.AMAUtils import AMAUtils
from MetagenomeUtils.authclient import KBaseAuth as _KBaseAuth
from installed_clients.AssemblyUtilClient import AssemblyUtil
from installed_clients.DataFileUtilClient import DataFileUtil
from installed_clients.WorkspaceClient import Workspace as workspaceService
from installed_clients.WsLargeDataIOClient import WsLargeDataIO


class AMAUtilsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        token = environ.get('KB_AUTH_TOKEN', None)
        config_file = environ.get('KB_DEPLOYMENT_CONFIG', None)
        cls.cfg = {}
        config = ConfigParser()
        config.read(config_file)
        for nameval in config.items('MetagenomeUtils'):
            cls.cfg[nameval[0]] = nameval[1]
        # Getting username from Auth profile for token
        authServiceUrl = cls.cfg['auth-service-url']
        auth_client = _KBaseAuth(authServiceUrl)
        user_id = auth_client.get_user(token)
        # WARNING: don't call any logging methods on the context object,
        # it'll result in a NoneType error
        cls.ctx = MethodContext(None)
        cls.ctx.update({'token': token,
                        'user_id': user_id,
                        'provenance': [
                            {'service': 'MetagenomeUtils',
                             'method': 'please_never_use_it_in_production',
                             'method_params': []
                             }],
                        'authenticated': 1})
        cls.wsURL = cls.cfg['workspace-url']
        cls.wsClient = workspaceService(cls.wsURL)
        cls.serviceImpl = MetagenomeUtils(cls.cfg)
        cls.scratch = cls.cfg['scratch']
        cls.callback_url = os.environ['SDK_CALLBACK_URL']
        suffix = int(time.time() * 1000)
        wsName = "test_kb_maxbin_" + str(suffix)
        cls.ws_info = cls.wsClient.create_workspace({'workspace': wsName})
        cls.dfu = DataFileUtil(os.environ['SDK_CALLBACK_URL'], token=token)
        cls.au = AssemblyUtil(os.environ['SDK_CALLBACK_URL'], token=token)

    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, 'wsName'):
            cls.wsClient.delete_workspace({'workspace': cls.wsName})
            print('Test workspace was deleted')

    def getWsClient(self):
        return self.__class__.wsClient

    def getWsName(self):
        return self.ws_info[1]

    def getWsID(self):
        return self.ws_info[0]

    def getImpl(self):
        return self.__class__.serviceImpl

    def getContext(self):
        return self.__class__.ctx

    def check_ret(self, ret, incl):
        self.assertTrue('genomes' in ret)
        data = ret.get('genomes')
        data = data[0]['data']
        for field in incl:
            self.assertTrue(field in data, msg=f"{field} not in returned output. Available fields {data.keys()}")
        # make sure one of the standard fields is not included
        self.assertFalse('features_handle_ref' in data)

    def save_metagenome(self):
        json_file = "Data/test_metagenome_object.json"
        with open(json_file) as f:
            data = json.load(f)
        data['assembly_ref'] = "22385/57/1"
        obj_info = self.dfu.save_objects({
            'id': self.getWsID(),
            "objects": [{
                'type': "KBaseMetagenomes.AnnotatedMetagenomeAssembly",
                'data': data,
                'name': "test_metagenome"
            }]
        })[0]
        return '/'.join([str(obj_info[6]), str(obj_info[0]), str(obj_info[4])])

    def test_get_ama(self):
        """"""
        appdev_ref = self.save_metagenome()

        incl = [
            'dna_size',
            'source_id',
            'genetic_code',
            'taxonomy',
            'genetic_code',
            'assembly_ref',
            'gc_content',
            'environment'
        ]
        params = {
            'ref': appdev_ref,
            'included_fields': incl,
            'included_feature_fields': []
        }

        ret = self.getImpl().get_annotated_metagenome_assembly(self.ctx, params)[0]
        self.check_ret(ret, incl)
