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

    /*
    Reference to a source_id
    @id external
    */
    typedef string source_id;

    /*
    Structure for a publication
    (float pubmedid
    string source (ex. Pubmed)
    string title
    string web address
    string publication year
    string authors
    string journal)
    */
    typedef tuple<float, string, string, string, string, string, string> publication;

    /*
    Reference to a ontology object
        @id ws KBaseOntology.OntologyDictionary
    */
    typedef string Ontology_ref;

    /*
    @optional ontology_ref method_version eco description
    */
    typedef structure {
        string id;
        Ontology_ref ontology_ref;
        string method;
        string method_version;
        string timestamp;
        string eco;
        string description;
    } Ontology_event;

    /*
    Reference to an Assembly object in the workspace
    @id ws KBaseGenomeAnnotations.Assembly
    */
    typedef string Assembly_ref;

    /*
    Reference to a handle to the Features JSON file on shock
        @id handle
    */
    typedef string features_handle_ref;

    /*
    Reference to a handle to the GFF file on shock
        @id handle
    */
    typedef string gff_handle_ref;

    /*
    Reference to a handle to protein FASTA file on shock
        @id handle
    */
    typedef string protein_handle_ref;

    typedef int Bool;

    /*
    The Metagenome object derives from Genome object in KBase but holds genetic 
    information from multiple organisms. It stores features in a single JSON array in SHOCK

    Genome publications should be papers about the genome
    Source: allowed entries RefSeq, Ensembl, Phytozome, RAST, Prokka, User_upload
    Warnings : mostly controlled vocab but also allow for unstructured

    Field Descriptions
        warnings - list of string - genome-level warnings generated in the annotation process
        feature_counts  - map of string to integer - total counts of each type of feature
            keys are a controlled vocabulary of - "CDS", "gene", "misc_feature",
            "misc_recomb", "mobile_element", "ncRNA" - 72, "non_coding_features",
            "non_coding_genes", "protein_encoding_gene", "rRNA", "rep_origin",
            "repeat_region", "tRNA"
        dna_size - integer - total number of nucleotides
        num_contigs - integer - total number of contigs in the metagenome
        num_features - integer - total number of features in the metagenome
        molecule_type - string - controlled vocab - the type of molecule sequenced
            Possible values are "Unknown", "DNA", "RNA", "genomic DNA", "genomic RNA",
            "mRNA", "tRNA", "rRNA", "other RNA", "other DNA", "transcribed RNA",
            "viral cRNA", "unassigned DNA", "unassigned RNA"
        contig_lengths - list of int - nucleotide length of each contig in the metagenome
            Indexes in this list correspond to indexes in the `contig_ids` list.
        contig_ids - list of str - external database identifiers for each contig (eg. "NC_000913.3")
        source - str - controlled vocab - descriptor of where this data came from (eg. "RefSeq")
            Allowed entries RefSeq, Ensembl, Phytozome, RAST, Prokka, User_upload
        source_id - string - identifier of this metagenome from the source database (eg. the RefSeq ID such as "NC_000913")
        md5 - string - checksum of the underlying assembly sequence
        gc_content - float - ratio of GC count to AT in the metagenome
        publications - tuple of (pubmedid, source, title, web_addr, year, authors, journal). See typedef above.
        ontology_events - A record of the service and method used for a set of
            ontology assignments on the metagenome.
        ontologies_present - a mapping of ontology source id (eg. "GO") to a mapping
            of term IDs (eg "GO:16209") to term names (eg. "histidine biosynthetic process").
        assembly_ref - workspace reference to an assembly object from which this annotated metagenome was derived.
        features_handle_ref -
            file server handle reference to the Annotated Metagenome Assebly features, stored as json. The resulting json file is a list of objects, where each object represents a feature. The features are modeled after those found in the Genome object (KBaseGenomes.Genome), but exclude any protein sequences. Each feature has the following fields:

                id - string - identifier of the feature, such as "b0001"
                type - string - type of feature, one of "cds", "non_coding_feature", "gene", ""
                location - list<tuple<string, int, string, int>> - list of
                    locations from where this sequence originates in the original assembly.
                    Each sub-sequence in the list constitutes a section of the resulting
                    CDS. The first element in the tuple corresponds to the "contig_id",
                    such as "NC_000913.3". The second element in the tuple is an index in
                    the contig of where the sequence starts. The third element is either a
                    plus or minus sign indicating whether it is on the 5' to 3' leading
                    strand ("+") or on the 3' to 5' lagging strand ("-"). The last element
                    is the length of the sub-sequence.
                    For a location on the leading strand (denoted by "+"), the index is
                    of the leftmost base, and the sequence extends to the right. For a
                    location on the lagging strand (denoted by "-"), the index is of
                    the rightmost base, and the sequence extends to the left.
                    NOTE: the last element in each tuple is the *length* of each
                    sub-sequence. If you have a location such as ("xyz", 100, "+", 50),
                    then your sequence will go from index 100 to index 149 (this has a
                    length of 50). It *does not* go from index 100 to index 150, as
                    that would have a length of 51.
                    Likewise, if you have the location ("xyz", 100, "-", 50), then the
                    sequence extends from 100 down to 51, which has a length of 50
                    bases. It does not go from index 100 to 50, as that would have a
                    length of 51.
                dna_sequence - dna sequence associated with this feature
                dna_sequence_length - length of the dna sequence associated with this feature.
                md5 - string - md5 of the dna sequence - TODO clarification
                aliases - list<(string, string)> - alternative list of names or identifiers
                    eg: [["gene", "thrA"], ["locus_tag", "b0002"]]
                warnings - list<string> - TODO
                cdss - optional - list<string> - list of corresponding coding sequence cds ids.
                parent_gene - optional - string - gene (feature) from which this CDS comes from,
                    including introns and UTRs that have been removed to create this CDS.
                functions - list<string> - list of protein products or chemical
                    processes that this sequence creates, facilitates, or influences.

        gff_handle_ref - file server handle reference to the source GFF file for this metagenome.
        protein_handle_ref
        external_source_origination_date
        release - string - User-supplied release or version of the source data. This
            most likely will come from an input field in the import app.
        original_source_file_name - filename from which this metagenome was derived (eg. genbank or gff filename).
        notes - TODO
        environment - string - environment to which this Metagenome refers. Not curently associated with any ontology (TODO)


    @optional warnings contig_lengths contig_ids source_id publications
    @optional ontology_events ontologies_present
    @optional gff_handle_ref external_source_origination_date
    @optional release original_source_file_name notes


    @metadata ws gc_content as GC content
    @metadata ws md5 as MD5
    @metadata ws dna_size as Size
    @metadata ws source_id as Source ID
    @metadata ws source as Source
    @metadata ws assembly_ref as Assembly Object
    @metadata ws num_contigs as Number contigs
    @metadata ws num_features as Number features
    @metadata ws length(warnings) as Number of Warnings
    @metadata ws environment as Environment
    @metadata ws feature_counts as FeatureCounts
    */
    typedef structure {
        list<string> warnings;
        mapping<string, int> feature_counts;
        int dna_size;
        int num_contigs;
        int num_features;
        string molecule_type;
        list<int> contig_lengths;
        list<string> contig_ids;
        string source;
        source_id source_id;
        string md5;
        float gc_content;
        list<publication> publications;
        list<Ontology_event> ontology_events;
        mapping<string, mapping<string, string>> ontologies_present;
        Assembly_ref assembly_ref;
        features_handle_ref features_handle_ref;
        gff_handle_ref gff_handle_ref;
        protein_handle_ref protein_handle_ref;
        string external_source_origination_date;
        string release;
        string original_source_file_name;
        string notes;
        string environment;
    } AnnotatedMetagenomeAssembly;

};
