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