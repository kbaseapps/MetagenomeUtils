class AMAUtils():

    def __init__(self, ws):
        self.ws = ws

    def _confirm_ws_type(self, ref):
        """confirm whether 'ref' is of type 'KBaseMetagenomes.AnnotatedMetagenomeAssembly
        if not, throw error. """
        if ref is None:
            raise ValueError(" 'ref' argument must be specified.")
        obj_info = self.ws.get_object_info3({
            'objects': [{'ref': ref}]
        })['infos'][0]
        # check object type is 'KBaseMetagenome.AnnotatedMetagenomeAssembly'
        obj_type = obj_info[2]
        if 'KBaseMetagenomes.AnnotatedMetagenomeAssembly' not in obj_type:
            raise ValueError(f"input ref '{ref}' is of type {obj_type}. function "
                            "'get_annotated_metagenome_assembly' requires objects"
                            " of type KBaseMetagenome.AnnotatedMetagenomeAssembly")

    def get_annotated_metagenome_assembly(self, params):
        """
        params:
            ref - workspace reference
            included_fields - list of fields to include, defaults to list below if not specified.
        output
            genomes - contains the returned data fields from the workspace request.

        """
        ref = params.get('ref', None)
        included_fields = params.get('included_fields', None)
        self._confirm_ws_type(ref)

        get_obj_params = {'ref': ref}
        if included_fields is not None:
            get_obj_params['included'] = included_fields

        data = self.ws.get_objects2({
            'objects': [get_obj_params]
        })['data']

        return {'genomes': data}
