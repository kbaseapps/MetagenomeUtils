/*
A KBase module for interacting with Metagenomic data in KBase
*/
module MetagenomeUtils {

    /* 
      An X/Y/Z style reference
    */
    typedef string obj_ref;

    /*
      file_directory: file directory containing compressed/unpacked contig file(s) to build BinnedContig object
      assembly_ref: Metagenome assembly object reference
      binned_contig_name: BinnedContig object name
      workspace_name: the name/id of the workspace it gets saved to
    */
    typedef structure {
      string file_directory;
      obj_ref assembly_ref;
      string binned_contig_name;
      string workspace_name;
    } FileToBinnedContigParams;

    typedef structure {
      obj_ref binned_contig_obj_ref;
    } FileToBinnedContigResult;

    /*
      file_to_binned_contigs: Generating BinnedContigs ojbect from files

      input params:
      file_directory: file directory containing compressed/unpacked contig file(s) to build BinnedContig object
      assembly_ref: Metagenome assembly object reference
      binned_contig_name: BinnedContig object name
      workspace_name: the name/id of the workspace it gets saved to

      return params:
      binned_contig_obj_ref: generated result BinnedContig object reference

    */
    funcdef file_to_binned_contigs(FileToBinnedContigParams params)
        returns (FileToBinnedContigResult returnVal) authentication required;

    /*
      input_ref: BinnedContig object reference
    */
    typedef structure {
      string input_ref;
    } ExportParams;

    typedef structure {
      string shock_id;
    } ExportOutput;

    /*
      binned_contigs_to_file: Convert BinnedContig object to fasta files and pack them to shock

      required params:
      input_ref: BinnedContig object reference

      return params:
      shock_id: saved packed file shock id
    */
    funcdef binned_contigs_to_file(ExportParams params)
        returns (ExportOutput returnVal) authentication required;

};
