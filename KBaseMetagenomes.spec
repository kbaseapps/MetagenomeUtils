module KBaseMetagenomes {

    typedef string bin_id;
    typedef string contig_id;

    /*
        Reference to an assembly object
        @id ws KBaseGenomeAnnotations.Assembly
    */
    typedef string assembly_ref;


    typedef structure {
        contig_id id;
    } Contig;

    typedef structure {
        bin_id bid;
        list<Contig> contigs;
    } ContigBin;

    /*
        Data type for tracking binned contigs in an Assembly
        @metadata ws assembly_ref
        @metadata ws length(bins) as n_bins
    */
    typedef structure {
        assembly_ref assembly_ref;
        list<ContigBin> bins;
    } BinnedContigs;

};