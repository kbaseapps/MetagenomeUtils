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
from MetagenomeUtils.authclient import KBaseAuth as _KBaseAuth
from installed_clients.AssemblyUtilClient import AssemblyUtil
from installed_clients.DataFileUtilClient import DataFileUtil
from installed_clients.WorkspaceClient import Workspace as workspaceService
from installed_clients.AbstractHandleClient import AbstractHandle as HandleService


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
        cls.metagenome_ref = None
        cls.handleURL = cls.cfg['handle-service-url']
        cls.hs = HandleService(cls.handleURL)
        cls.object_ref = 'KBaseTestData/test_metagenome/1'

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

    def _check_features(self, features, feat_type=None, only_ids=False):
        for item in features:
            self.assertTrue('id' in item)
            if not only_ids:
                self.assertTrue('type' in item)
                self.assertTrue('location' in item)
                self.assertTrue('dna_sequence' in item)
                if feat_type:
                    self.assertTrue(item['type'].lower() == feat_type.lower())
            else:
                self.assertTrue('type' not in item)
                self.assertTrue('location' not in item)
                self.assertTrue('dna_sequence' not in item)

    def _check_ret(self, ret, incl):
        self.assertTrue('genomes' in ret)
        data = ret.get('genomes')
        data = data[0]['data']
        for field in incl:
            self.assertTrue(field in data, msg=f"{field} not in returned output. Available fields {data.keys()}")
        # make sure one of the standard fields is not included
        self.assertFalse('features_handle_ref' in data)

    def test_get_ama(self):
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
            'ref': self.object_ref,
            'included_fields': incl,
            'included_feature_fields': []
        }

        ret = self.getImpl().get_annotated_metagenome_assembly(self.ctx, params)[0]
        self._check_ret(ret, incl)

    # @unittest.skip('x')
    def test_get_ama_features(self):
        ret = self.getImpl().get_annotated_metagenome_assembly_features(
            self.ctx,
            {'ref': self.object_ref}
        )[0]
        self._check_features(ret['features'])

    # @unittest.skip('x')
    def test_get_ama_features_with_type(self):
        feat_type = 'cds'
        ret = self.getImpl().get_annotated_metagenome_assembly_features(
            self.ctx,
            {
                'ref': self.object_ref,
                'feature_type': 'cds'
            }
        )[0]
        self._check_features(ret['features'], feat_type=feat_type)

    # @unittest.skip('x')
    def test_get_ama_features_only_ids(self):
        feat_type = 'cds'
        ret = self.getImpl().get_annotated_metagenome_assembly_features(
            self.ctx,
            {
                'ref': self.object_ref,
                'only_ids': 1
            }
        )[0]
        self._check_features(ret['features'], only_ids=True)
