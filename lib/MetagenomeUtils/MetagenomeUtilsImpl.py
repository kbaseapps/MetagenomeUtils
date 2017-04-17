# -*- coding: utf-8 -*-
#BEGIN_HEADER
import os
import json

from MetagenomeUtils.Utils.MetagenomeFileUtils import MetagenomeFileUtils
#END_HEADER


class MetagenomeUtils:
    '''
    Module Name:
    MetagenomeUtils

    Module Description:
    A KBase module for interacting with Metagenomic data in KBase
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.2"
    GIT_URL = "https://github.com/Tianhao-Gu/MetagenomeUtils.git"
    GIT_COMMIT_HASH = "a175fd5e148b8f2468bc8f0332d562aac5ecea8d"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.config = config
        self.config['SDK_CALLBACK_URL'] = os.environ['SDK_CALLBACK_URL']
        self.config['KB_AUTH_TOKEN'] = os.environ['KB_AUTH_TOKEN']
        #END_CONSTRUCTOR
        pass


    def file_to_binned_contigs(self, ctx, params):
        """
        file_to_binned_contigs: Generating BinnedContigs ojbect from files
        input params:
        file_directory: file directory containing compressed/unpacked contig file(s) to build BinnedContig object
        assembly_ref: Metagenome assembly object reference
        binned_contig_name: BinnedContig object name
        workspace_name: the name/id of the workspace it gets saved to
        return params:
        binned_contig_obj_ref: generated result BinnedContig object reference
        :param params: instance of type "FileToBinnedContigParams"
           (file_directory: file directory containing compressed/unpacked
           contig file(s) to build BinnedContig object assembly_ref:
           Metagenome assembly object reference binned_contig_name:
           BinnedContig object name workspace_name: the name/id of the
           workspace it gets saved to) -> structure: parameter
           "file_directory" of String, parameter "assembly_ref" of type
           "obj_ref" (An X/Y/Z style reference), parameter
           "binned_contig_name" of String, parameter "workspace_name" of
           String
        :returns: instance of type "FileToBinnedContigResult" -> structure:
           parameter "binned_contig_obj_ref" of type "obj_ref" (An X/Y/Z
           style reference)
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN file_to_binned_contigs
        print '--->\nRunning MetagenomeUtils.file_to_binned_contigs\nparams:'
        print json.dumps(params, indent=1)

        for key, value in params.iteritems():
            if isinstance(value, basestring):
                params[key] = value.strip()

        binned_contig_builder = MetagenomeFileUtils(self.config)
        returnVal = binned_contig_builder.file_to_binned_contigs(params)
        #END file_to_binned_contigs

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method file_to_binned_contigs return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def binned_contigs_to_file(self, ctx, params):
        """
        binned_contigs_to_file: Convert BinnedContig object to fasta files and pack them to shock
        required params:
        input_ref: BinnedContig object reference
        optional params:
        not_save_to_shock: not saving result bin files to shock
        return params:
        shock_id: saved packed file shock id (None if not_save_to_shock is set)
        bin_file_list: a list of bin file path
        :param params: instance of type "ExportParams" (input_ref:
           BinnedContig object reference optional params: not_save_to_shock:
           not saving result bin files to shock) -> structure: parameter
           "input_ref" of String, parameter "not_save_to_shock" of type
           "boolean" (A boolean - 0 for false, 1 for true. @range (0, 1))
        :returns: instance of type "ExportOutput" (shock_id: saved packed
           file shock id bin_file_list: a list of bin file path) ->
           structure: parameter "shock_id" of String, parameter
           "bin_file_list" of list of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN binned_contigs_to_file
        print '--->\nRunning MetagenomeUtils.binned_contigs_to_file\nparams:'
        print json.dumps(params, indent=1)

        for key, value in params.iteritems():
            if isinstance(value, basestring):
                params[key] = value.strip()

        binned_contig_downloader = MetagenomeFileUtils(self.config)
        returnVal = binned_contig_downloader.binned_contigs_to_file(params)
        #END binned_contigs_to_file

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method binned_contigs_to_file return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def extract_binned_contigs_as_assembly(self, ctx, params):
        """
        extract_binned_contigs_as_assembly: extract one/multiple Bins from BinnedContigs as Assembly object
        input params:
        binned_contig_obj_ref: BinnedContig object reference
        extracted_assemblies: a list of:
              bin_id: target bin id to be extracted
              output_assembly_name: output assembly object name
        workspace_name: the name of the workspace it gets saved to
        return params:
        assembly_ref_list: list of generated result Assembly object reference
        report_name: report name generated by KBaseReport
        report_ref: report reference generated by KBaseReport
        :param params: instance of type "ExtractBinAsAssemblyParams"
           (binned_contig_obj_ref: BinnedContig object reference
           extracted_assemblies: a list of: bin_id: target bin id to be
           extracted output_assembly_name: output assembly object name
           workspace_name: the name of the workspace it gets saved to) ->
           structure: parameter "binned_contig_obj_ref" of type "obj_ref" (An
           X/Y/Z style reference), parameter "bin_id" of String, parameter
           "output_assembly_name" of String, parameter "extracted_assemblies"
           of list of mapping from String to String, parameter
           "workspace_name" of String
        :returns: instance of type "ExtractBinAsAssemblyResult"
           (assembly_ref_list: list of generated Assembly object reference
           report_name: report name generated by KBaseReport report_ref:
           report reference generated by KBaseReport) -> structure: parameter
           "assembly_ref_list" of list of type "obj_ref" (An X/Y/Z style
           reference), parameter "report_name" of String, parameter
           "report_ref" of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN extract_binned_contigs_as_assembly
        print '--->\nRunning MetagenomeUtils.extract_binned_contigs_as_assembly\nparams:'
        print json.dumps(params, indent=1)

        for key, value in params.iteritems():
            if isinstance(value, basestring):
                params[key] = value.strip()

        binned_contig_extractor = MetagenomeFileUtils(self.config)
        returnVal = binned_contig_extractor.extract_binned_contigs_as_assembly(params)
        #END extract_binned_contigs_as_assembly

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method extract_binned_contigs_as_assembly return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
