from installed_clients.WorkspaceClient import Workspace
from installed_clients.DataFileUtilClient import DataFileUtil
import json
import os


class AMAUtils():

    def __init__(self, ws_url, cb_url, token, scratch):
        self.ws = Workspace(ws_url, token=token)
        self.cb_url = cb_url
        self.token = token
        self.scratch = scratch

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

    def get_annotated_metagenome_assembly_features(self, params):
        """
        params: 
            ref - workspace reference for KBaseMetagenomes.AnnotatedMetagenomeAssembly object
        output:
            features - list of features, each representing a dict.
        """
        ref = params['ref']
        self._confirm_ws_type(ref)
        ret = self.ws.get_objects2({
            "objects": [{
                "ref": ref,
                "included": [
                    "features_handle_ref"
                ]
            }]
        })['data']
        features_handle_ref = ret[0]['data']['features_handle_ref']
        dfu = DataFileUtil(self.cb_url, token=self.token)
        file_name = 'features.json.gz'
        file_path = os.path.join(self.scratch, file_name)
        shock_ret = dfu.shock_to_file({
            'handle_id': features_handle_ref,
            'file_path': file_path,
            'unpack': "uncompress"
        })
        file_path = shock_ret['file_path']

        with open(file_path) as fd:
            json_features = json.load(fd)

        if params.get('feature_type'):
            accepted_feature_types = [
                "cds",
                "gene",
                "mrna",
                "trna",
                "rrna",
                "repeat_region"
            ]
            feat_type = params['feature_type']
            if feat_type.lower() not in accepted_feature_types:
                raise ValueError(f"{feat_type} not an accepted feature type; accepted feature"
                                 " types (in lower case) are {accepted_feature_types}")
            json_features = [feature for feature in json_features if feature['type'].lower() == feat_type.lower()]

        if params.get('only_ids'):
            json_features = [{'id': feature['id']} for feature in json_features]

        return {'features': json_features}
