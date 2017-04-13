module KBaseMetagenomes {

    typedef string bin_id;
    typedef string contig_id;

    /*
        Reference to an assembly object
        @id ws KBaseGenomeAnnotations.Assembly
    */
    typedef string assembly_ref;


    /*
        gc (float)           - GC content
        len (int)            - length in bp of the contig
        cov (float)          - optional coverage
        @optional cov
    */
    typedef structure {
        float gc;
        int len;
        float cov;
    } Contig;

    /*
        bid (string) - ID of the bin
        contigs      - A map from contig_id to information on the contig

        gc (float)           - total GC content of the contigs (ie, concatenate all
                               the contigs and compute the GC content)
        sum_contig_len (int) - cumulative length in bp of all the contigs in this bin
        cov (float)          - total coverage over all contigs(ie, the avg coverage
                               weighted by contig length
        @optional cov
    */
    typedef structure {
        bin_id bid;
        mapping<contig_id, Contig> contigs;
        int n_contigs;
        float gc;
        int sum_contig_len;
        float cov;
    } ContigBin;

    /*
        Data type for tracking binned contigs in an Assembly
        @metadata ws assembly_ref
        @metadata ws total_contig_len
        @metadata ws length(bins) as n_bins
    */
    typedef structure {
        assembly_ref assembly_ref;
        list<ContigBin> bins;
        int total_contig_len;
    } BinnedContigs;

};