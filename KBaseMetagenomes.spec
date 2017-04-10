


module KBaseMetagenomes {

    typedef string bin_id;
    typedef string contig_id;

    /*
     Reference to an assembly object
     @id ws KBaseGenomeAnnotations.Assembly
    */
    typedef string contig_obj_ref;

    typedef structure {
        list<bin_id> bin_ids;
        mapping<bin_id, list<contig_id>> bin2contig_id;
        mapping<contig_id, contig_obj_ref> contig_id2contig_ref;
    } BinnedAssembly;


};
