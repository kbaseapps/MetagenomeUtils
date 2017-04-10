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

    /*
        bid (string) - ID of the bin
        contigs      - The list of contigs mapped to this bin

        gc (float)   - GC content of the contigs
        len (int)    - cumulative length in bp of all the contigs in this bin
        cov (float)  - optional coverage value
        @optional cov
    */
    typedef structure {
        bin_id bid;
        list<Contig> contigs;
        float gc;
        int len;
        float cov;
    } ContigBin;

    /*
        Data type for tracking binned contigs in an Assembly
        @metadata ws assembly_ref
        @metadata ws total_len
        @metadata ws length(bins) as n_bins
    */
    typedef structure {
        assembly_ref assembly_ref;
        list<ContigBin> bins;
        int total_len;
    } BinnedContigs;

};