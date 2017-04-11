# -*- coding: utf-8 -*-
import unittest
import os  # noqa: F401
import json  # noqa: F401
import time
import requests  # noqa: F401
import shutil

from os import environ
try:
    from ConfigParser import ConfigParser  # py2
except:
    from configparser import ConfigParser  # py3

from pprint import pprint  # noqa: F401

from biokbase.workspace.client import Workspace as workspaceService
from MetagenomeUtils.MetagenomeUtilsImpl import MetagenomeUtils
from MetagenomeUtils.MetagenomeUtilsServer import MethodContext
from MetagenomeUtils.authclient import KBaseAuth as _KBaseAuth
from MetagenomeUtils.Utils.MetagenomeFileUtils import MetagenomeFileUtils
from DataFileUtil.DataFileUtilClient import DataFileUtil
from AssemblyUtil.AssemblyUtilClient import AssemblyUtil


class MetagenomeUtilsTest(unittest.TestCase):

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
        cls.binned_contig_builder = MetagenomeFileUtils(cls.cfg)
        cls.prepare_data()

    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, 'wsName'):
            cls.wsClient.delete_workspace({'workspace': cls.wsName})
            print('Test workspace was deleted')

    @classmethod
    def prepare_data(cls):
        test_directory_name = 'test_MetagenomeFileUtils'
        cls.test_directory_path = os.path.join(cls.scratch, test_directory_name)
        os.makedirs(cls.test_directory_path)

        for item in os.listdir(os.path.join("Data", "MaxBin_Result_Sample")):
            shutil.copy(os.path.join("Data", "MaxBin_Result_Sample", item),
                        os.path.join(cls.test_directory_path, item))

        # building Assembly
        assembly_filename = 'small_bin_contig_file.fasta'
        cls.assembly_fasta_file_path = os.path.join(cls.scratch, assembly_filename)
        shutil.copy(os.path.join("Data", assembly_filename), cls.assembly_fasta_file_path)

        assembly_params = {
            'file': {'path': cls.assembly_fasta_file_path},
            'workspace_name': cls.ws_info[1],
            'assembly_name': 'MyAssembly'
        }
        cls.assembly_ref = cls.au.save_assembly_from_fasta(assembly_params)

    def getWsClient(self):
        return self.__class__.wsClient

    def getWsName(self):
        return self.ws_info[1]

    def getImpl(self):
        return self.__class__.serviceImpl

    def getContext(self):
        return self.__class__.ctx

    def test_bad_file_to_binned_contigs_params(self):
        invalidate_input_params = {
            'missing_assembly_ref': 'assembly_ref',
            'file_directory': 'file_directory',
            'binned_contig_name': 'binned_contig_name',
            'workspace_name': 'workspace_name'

        }
        with self.assertRaisesRegexp(
                    ValueError, '"assembly_ref" parameter is required, but missing'):
            self.getImpl().file_to_binned_contigs(self.getContext(), invalidate_input_params)

        invalidate_input_params = {
            'assembly_ref': 'assembly_ref',
            'missing_file_directory': 'file_directory',
            'binned_contig_name': 'binned_contig_name',
            'workspace_name': 'workspace_name'

        }
        with self.assertRaisesRegexp(
                    ValueError, '"file_directory" parameter is required, but missing'):
            self.getImpl().file_to_binned_contigs(self.getContext(), invalidate_input_params)

        invalidate_input_params = {
            'assembly_ref': 'assembly_ref',
            'file_directory': 'file_directory',
            'missing_binned_contig_name': 'binned_contig_name',
            'workspace_name': 'workspace_name'

        }
        with self.assertRaisesRegexp(
                    ValueError, '"binned_contig_name" parameter is required, but missing'):
            self.getImpl().file_to_binned_contigs(self.getContext(), invalidate_input_params)

        invalidate_input_params = {
            'assembly_ref': 'assembly_ref',
            'file_directory': 'file_directory',
            'binned_contig_name': 'binned_contig_name',
            'missing_workspace_name': 'workspace_name'

        }
        with self.assertRaisesRegexp(
                    ValueError, '"workspace_name" parameter is required, but missing'):
            self.getImpl().file_to_binned_contigs(self.getContext(), invalidate_input_params)

    def test_MetagenomeFileUtils_get_bin_ids(self):

        file_directory = self.test_directory_path
        bin_ids = self.binned_contig_builder._get_bin_ids(file_directory)

        expect_bin_ids_set = set(['out_header.001.fasta',
                                  'out_header.002.fasta',
                                  'out_header.003.fasta'])

        self.assertEquals(set(bin_ids), expect_bin_ids_set)

    def test_MetagenomeFileUtil_generate_contig_bin_summary(self):

        bin_id = 'out_header.003.fasta'
        file_directory = self.test_directory_path

        gc, sum_contig_len, cov = self.binned_contig_builder._generate_contig_bin_summary(
                                                                                    bin_id,
                                                                                    file_directory)

        self.assertEquals(gc, 54.8)
        self.assertEquals(sum_contig_len, 2452188)
        self.assertEquals(cov, 92.5)

        bin_id = 'out_header.001.fasta'
        file_directory = self.test_directory_path

        gc, sum_contig_len, cov = self.binned_contig_builder._generate_contig_bin_summary(
                                                                                    bin_id,
                                                                                    file_directory)

        self.assertEquals(gc, 52.9)
        self.assertEquals(sum_contig_len, 2674902)
        self.assertEquals(cov, 100.0)

    def test_MetagenomeFileUtil_generate_string_contigs(self):

        bin_id = 'small_bin_contig_file.fasta'

        test_directory_name = 'test_MetagenomeFileUtils_generate_string_contigs'
        test_directory_path = os.path.join(self.scratch, test_directory_name)
        os.makedirs(test_directory_path)

        shutil.copy(os.path.join("Data", bin_id), os.path.join(test_directory_path, bin_id))

        string_contigs = self.binned_contig_builder._generate_string_contigs(bin_id,
                                                                             test_directory_path)

        self.assertEquals(len(string_contigs), 8)

    def test_MetagenomeFileUtil_generate_contig_summary(self):

        string_contig = '>NODE_9_length_4254_cov_19.036436\n'
        string_contig += 'TTAAGGCC\n'
        string_contig += 'TTAAGGCCTTAAGGCC\n'

        contig_id, contig_gc, contig_len = self.binned_contig_builder._generate_contig_summary(
                                                                                    string_contig)

        self.assertEquals(contig_id, 'NODE_9_length_4254_cov_19.036436')
        self.assertEquals(contig_gc, 0.5)
        self.assertEquals(contig_len, 24)

    def test_MetagenomeFileUtil_generate_contig_bin(self):
        bin_id = 'out_header.003.fasta'
        file_directory = self.test_directory_path

        contig_bin = self.binned_contig_builder._generate_contig_bin(bin_id, file_directory)

        expect_bin_keys = ['contigs', 'bid', 'gc', 'sum_contig_len', 'cov']
        self.assertItemsEqual(contig_bin.keys(), expect_bin_keys)
        self.assertEquals(contig_bin.get('bid'), bin_id)

        expect_contig_bin_keys = ['gc', 'id', 'len']
        self.assertItemsEqual(contig_bin.get('contigs')[0].keys(), expect_contig_bin_keys)

    def test_file_to_binned_contigs(self):

        binned_contig_name = 'MyBinnedContig'
        params = {
            'assembly_ref': self.assembly_ref,
            'file_directory': self.test_directory_path,
            'binned_contig_name': binned_contig_name,
            'workspace_name': self.dfu.ws_name_to_id(self.getWsName())
        }

        resultVal = self.getImpl().file_to_binned_contigs(self.getContext(), params)[0]
        self.assertTrue('binned_contig_obj_ref' in resultVal)

        binned_contig_object = self.dfu.get_objects(
                        {'object_refs': [self.getWsName() + '/MyBinnedContig']})['data'][0]

        binned_contig_info = binned_contig_object.get('info')

        self.assertEquals(binned_contig_info[1], binned_contig_name)
        expect_binned_contig_info_list = ['assembly_ref', 'total_contig_len', 'n_bins']
        self.assertItemsEqual(binned_contig_info[-1], expect_binned_contig_info_list)
        self.assertEquals(int(binned_contig_info[-1].get('n_bins')), 3)
        self.assertEquals(binned_contig_info[-1].get('assembly_ref'), self.assembly_ref)
        self.assertEquals(int(binned_contig_info[-1].get('total_contig_len')), 8397583)

        binned_contig_data = binned_contig_object.get('data')
        epxect_binned_contig_keys = ['total_contig_len', 'assembly_ref', 'bins']
        self.assertItemsEqual(binned_contig_data.keys(), epxect_binned_contig_keys)
        self.assertEquals(binned_contig_data.get('total_contig_len'), 8397583)
        self.assertEquals(binned_contig_data.get('assembly_ref'), self.assembly_ref)

        expect_bin_keys = ['contigs', 'bid', 'gc', 'sum_contig_len', 'cov']
        self.assertItemsEqual(binned_contig_data.get('bins')[0].keys(), expect_bin_keys)
