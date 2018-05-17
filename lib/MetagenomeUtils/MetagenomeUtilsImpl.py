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
    VERSION = "1.0.2"
    GIT_URL = "https://github.com/Tianhao-Gu/MetagenomeUtils.git"
    GIT_COMMIT_HASH = "eae661df685d85b94e074948e8797276b4bcb89e"

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
        save_to_shock: saving result bin files to shock. default to True
        return params:
        shock_id: saved packed file shock id (None if save_to_shock is set to False)
        bin_file_directory: directory that contains all bin files
        :param params: instance of type "ExportParams" (input_ref:
           BinnedContig object reference optional params: save_to_shock:
           saving result bin files to shock. default to True) -> structure:
           parameter "input_ref" of String, parameter "save_to_shock" of type
           "boolean" (A boolean - 0 for false, 1 for true. @range (0, 1))
        :returns: instance of type "ExportOutput" (shock_id: saved packed
           file shock id bin_file_directory: directory that contains all bin
           files) -> structure: parameter "shock_id" of String, parameter
           "bin_file_directory" of String
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

    def export_binned_contigs_as_excel(self, ctx, params):
        """
        export_binned_contigs_as_excel: Convert BinnedContig object to an excel file and pack it to shock
        required params:
        input_ref: BinnedContig object reference
        optional params:
        save_to_shock: saving result bin files to shock. default to True
        return params:
        shock_id: saved packed file shock id (None if save_to_shock is set to False)
        bin_file_directory: directory that contains all bin files
        :param params: instance of type "ExportParams" (input_ref:
           BinnedContig object reference optional params: save_to_shock:
           saving result bin files to shock. default to True) -> structure:
           parameter "input_ref" of String, parameter "save_to_shock" of type
           "boolean" (A boolean - 0 for false, 1 for true. @range (0, 1))
        :returns: instance of type "ExportOutput" (shock_id: saved packed
           file shock id bin_file_directory: directory that contains all bin
           files) -> structure: parameter "shock_id" of String, parameter
           "bin_file_directory" of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN export_binned_contigs_as_excel
        print '--->\nRunning MetagenomeUtils.export_binned_contigs_as_excel\nparams:'
        print json.dumps(params, indent=1)

        for key, value in params.iteritems():
            if isinstance(value, basestring):
                params[key] = value.strip()

        binned_contig_downloader = MetagenomeFileUtils(self.config)
        returnVal = binned_contig_downloader.export_binned_contigs_as_excel(params)
        #END export_binned_contigs_as_excel

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method export_binned_contigs_as_excel return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def import_excel_as_binned_contigs(self, ctx, params):
        """
        import_excel_as_binned_contigs: Import an excel file as BinnedContigs
        required params:
        shock_id: Excel file stored in shock
        workspace_name: the name of the workspace object gets saved to
        optional params:
        binned_contigs_name: saved BinnedContig name. 
                             Auto append timestamp from excel if not given.
        :param params: instance of type "ImportExcelParams" -> structure:
           parameter "shock_id" of String, parameter "workspace_name" of
           String, parameter "binned_contigs_name" of String
        :returns: instance of type "ImportExcelOutput" -> structure:
           parameter "report_name" of String, parameter "report_ref" of
           String, parameter "binned_contigs_ref" of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN import_excel_as_binned_contigs
        print '--->\nRunning MetagenomeUtils.import_excel_as_binned_contigs\nparams:'
        print json.dumps(params, indent=1)

        for key, value in params.iteritems():
            if isinstance(value, basestring):
                params[key] = value.strip()

        binned_contig_importer = MetagenomeFileUtils(self.config)
        returnVal = binned_contig_importer.import_excel_as_binned_contigs(params)
        #END import_excel_as_binned_contigs

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method import_excel_as_binned_contigs return value ' +
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
              assembly_suffix: suffix appended to assembly object name
        workspace_name: the name of the workspace it gets saved to
        return params:
        assembly_ref_list: list of generated result Assembly object reference
        report_name: report name generated by KBaseReport
        report_ref: report reference generated by KBaseReport
        :param params: instance of type "ExtractBinAsAssemblyParams"
           (binned_contig_obj_ref: BinnedContig object reference
           extracted_assemblies: a list of dictionaries: bin_id: target bin
           id to be extracted assembly_suffix: suffix appended to assembly
           object name assembly_set_name:  name for created assembly set
           workspace_name: the name of the workspace it gets saved to) ->
           structure: parameter "binned_contig_obj_ref" of type "obj_ref" (An
           X/Y/Z style reference), parameter "extracted_assemblies" of
           String, parameter "assembly_suffix" of String, parameter
           "assembly_set_name" of String, parameter "workspace_name" of String
        :returns: instance of type "ExtractBinAsAssemblyResult"
           (assembly_ref_list: list of generated Assembly object reference
           report_name: report name generated by KBaseReport report_ref:
           report reference generated by KBaseReport) -> structure: parameter
           "assembly_ref_list" of list of type "obj_ref" (An X/Y/Z style
           reference), parameter "report_name" of String, parameter
           "report_ref" of String, parameter "assembly_set_ref" of String
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

    def remove_bins_from_binned_contig(self, ctx, params):
        """
        remove_bins_from_binned_contig: remove a list of bins from BinnedContig object
        input params:
        old_binned_contig_ref: Original BinnedContig object reference
        bins_to_remove: a list of bin ids to be removed
        output_binned_contig_name: Name for the output BinnedContigs object
        workspace_name: the name of the workspace new object gets saved to
        return params:
        new_binned_contig_ref: newly created BinnedContig object referece
        :param params: instance of type "RemoveBinsParams"
           (old_binned_contig_ref: Original BinnedContig object reference
           bins_to_remove: a list of bin ids to be removed
           output_binned_contig_name: Name for the output BinnedContigs
           object workspace_name: the name of the workspace new object gets
           saved to) -> structure: parameter "old_binned_contig_ref" of type
           "obj_ref" (An X/Y/Z style reference), parameter "bins_to_remove"
           of list of String, parameter "output_binned_contig_name" of
           String, parameter "workspace_name" of String
        :returns: instance of type "RemoveBinsResult" (new_binned_contig_ref:
           newly created BinnedContig object referece report_name: report
           name generated by KBaseReport report_ref: report reference
           generated by KBaseReport) -> structure: parameter
           "new_binned_contig_ref" of type "obj_ref" (An X/Y/Z style
           reference)
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN remove_bins_from_binned_contig
        print '--->\nRunning MetagenomeUtils.remove_bins_from_binned_contig\nparams:'
        print json.dumps(params, indent=1)

        for key, value in params.iteritems():
            if isinstance(value, basestring):
                params[key] = value.strip()

        binned_contig_remover = MetagenomeFileUtils(self.config)
        returnVal = binned_contig_remover.remove_bins_from_binned_contig(params)
        #END remove_bins_from_binned_contig

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method remove_bins_from_binned_contig return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def merge_bins_from_binned_contig(self, ctx, params):
        """
        merge_bins_from_binned_contig: merge a list of bins from BinnedContig object
        input params:
        old_binned_contig_ref: Original BinnedContig object reference
        bin_merges: a list of bin merges dicts
          new_bin_id: newly created bin id
          bin_to_merge: list of bins to merge
        output_binned_contig_name: Name for the output BinnedContigs object
        workspace_name: the name of the workspace new object gets saved to
        return params:
        new_binned_contig_ref: newly created BinnedContig object referece
        :param params: instance of type "MergeBinsParams"
           (old_binned_contig_ref: Original BinnedContig object reference
           bin_merges: a list of bin merges dicts new_bin_id: newly created
           bin id bin_to_merge: list of bins to merge
           output_binned_contig_name: Name for the output BinnedContigs
           object workspace_name: the name of the workspace new object gets
           saved to) -> structure: parameter "old_binned_contig_ref" of type
           "obj_ref" (An X/Y/Z style reference), parameter "bin_merges" of
           list of mapping from String to String, parameter
           "output_binned_contig_name" of String, parameter "workspace_name"
           of String
        :returns: instance of type "MergeBinsResult" (new_binned_contig_ref:
           newly created BinnedContig object referece) -> structure:
           parameter "new_binned_contig_ref" of type "obj_ref" (An X/Y/Z
           style reference)
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN merge_bins_from_binned_contig
        print '--->\nRunning MetagenomeUtils.merge_bins_from_binned_contig\nparams:'
        print json.dumps(params, indent=1)

        for key, value in params.iteritems():
            if isinstance(value, basestring):
                params[key] = value.strip()

        binned_contig_merger = MetagenomeFileUtils(self.config)
        returnVal = binned_contig_merger.merge_bins_from_binned_contig(params)
        #END merge_bins_from_binned_contig

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method merge_bins_from_binned_contig return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def edit_bins_from_binned_contig(self, ctx, params):
        """
        edit_bins_from_binned_contig: merge/remove a list of bins from BinnedContig object
        a wrapper method of:
        merge_bins_from_binned_contig
        remove_bins_from_binned_contig
        input params:
        old_binned_contig_ref: Original BinnedContig object reference
        bins_to_remove: a list of bin ids to be removed
        bin_merges: a list of bin merges dicts
          new_bin_id: newly created bin id
          bin_to_merge: list of bins to merge
        output_binned_contig_name: Name for the output BinnedContigs object
        workspace_name: the name of the workspace new object gets saved to
        return params:
        new_binned_contig_ref: newly created BinnedContig object referece
        report_name: report name generated by KBaseReport
        report_ref: report reference generated by KBaseReport
        :param params: instance of type "EditBinsParams"
           (old_binned_contig_ref: Original BinnedContig object reference
           bins_to_remove: a list of bin ids to be removed bin_merges: a list
           of bin merges dicts new_bin_id: newly created bin id bin_to_merge:
           list of bins to merge output_binned_contig_name: Name for the
           output BinnedContigs object workspace_name: the name of the
           workspace new object gets saved to) -> structure: parameter
           "old_binned_contig_ref" of type "obj_ref" (An X/Y/Z style
           reference), parameter "bins_to_remove" of list of String,
           parameter "bin_merges" of list of mapping from String to String,
           parameter "output_binned_contig_name" of String, parameter
           "workspace_name" of String
        :returns: instance of type "EditBinsResult" (new_binned_contig_ref:
           newly created BinnedContig object referece report_name: report
           name generated by KBaseReport report_ref: report reference
           generated by KBaseReport) -> structure: parameter
           "new_binned_contig_ref" of type "obj_ref" (An X/Y/Z style
           reference), parameter "report_name" of String, parameter
           "report_ref" of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN edit_bins_from_binned_contig
        print '--->\nRunning MetagenomeUtils.edit_bins_from_binned_contig\nparams:'
        print json.dumps(params, indent=1)

        for key, value in params.iteritems():
            if isinstance(value, basestring):
                params[key] = value.strip()

        binned_contig_editor = MetagenomeFileUtils(self.config)
        returnVal = binned_contig_editor.edit_bins_from_binned_contig(params)
        #END edit_bins_from_binned_contig

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method edit_bins_from_binned_contig return value ' +
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
