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
    VERSION = "0.0.1"
    GIT_URL = "https://github.com/Tianhao-Gu/MetagenomeUtils.git"
    GIT_COMMIT_HASH = "a8559529c21972e60e074d524a42c7937b7f25e0"

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
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
