
package us.kbase.metagenomeutils;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import javax.annotation.Generated;
import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * <p>Original spec-file type: ExtractBinAsAssemblyParams</p>
 * <pre>
 * binned_contig_obj_ref: BinnedContig object reference
 * extracted_assemblies: a list of dictionaries:
 *       bin_id: target bin id to be extracted
 * assembly_suffix: suffix appended to assembly object name
 * assembly_set_name:  name for created assembly set
 * workspace_name: the name of the workspace it gets saved to
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "binned_contig_obj_ref",
    "extracted_assemblies",
    "assembly_suffix",
    "assembly_set_name",
    "workspace_name"
})
public class ExtractBinAsAssemblyParams {

    @JsonProperty("binned_contig_obj_ref")
    private java.lang.String binnedContigObjRef;
    @JsonProperty("extracted_assemblies")
    private List<Map<String, String>> extractedAssemblies;
    @JsonProperty("assembly_suffix")
    private java.lang.String assemblySuffix;
    @JsonProperty("assembly_set_name")
    private java.lang.String assemblySetName;
    @JsonProperty("workspace_name")
    private java.lang.String workspaceName;
    private Map<java.lang.String, Object> additionalProperties = new HashMap<java.lang.String, Object>();

    @JsonProperty("binned_contig_obj_ref")
    public java.lang.String getBinnedContigObjRef() {
        return binnedContigObjRef;
    }

    @JsonProperty("binned_contig_obj_ref")
    public void setBinnedContigObjRef(java.lang.String binnedContigObjRef) {
        this.binnedContigObjRef = binnedContigObjRef;
    }

    public ExtractBinAsAssemblyParams withBinnedContigObjRef(java.lang.String binnedContigObjRef) {
        this.binnedContigObjRef = binnedContigObjRef;
        return this;
    }

    @JsonProperty("extracted_assemblies")
    public List<Map<String, String>> getExtractedAssemblies() {
        return extractedAssemblies;
    }

    @JsonProperty("extracted_assemblies")
    public void setExtractedAssemblies(List<Map<String, String>> extractedAssemblies) {
        this.extractedAssemblies = extractedAssemblies;
    }

    public ExtractBinAsAssemblyParams withExtractedAssemblies(List<Map<String, String>> extractedAssemblies) {
        this.extractedAssemblies = extractedAssemblies;
        return this;
    }

    @JsonProperty("assembly_suffix")
    public java.lang.String getAssemblySuffix() {
        return assemblySuffix;
    }

    @JsonProperty("assembly_suffix")
    public void setAssemblySuffix(java.lang.String assemblySuffix) {
        this.assemblySuffix = assemblySuffix;
    }

    public ExtractBinAsAssemblyParams withAssemblySuffix(java.lang.String assemblySuffix) {
        this.assemblySuffix = assemblySuffix;
        return this;
    }

    @JsonProperty("assembly_set_name")
    public java.lang.String getAssemblySetName() {
        return assemblySetName;
    }

    @JsonProperty("assembly_set_name")
    public void setAssemblySetName(java.lang.String assemblySetName) {
        this.assemblySetName = assemblySetName;
    }

    public ExtractBinAsAssemblyParams withAssemblySetName(java.lang.String assemblySetName) {
        this.assemblySetName = assemblySetName;
        return this;
    }

    @JsonProperty("workspace_name")
    public java.lang.String getWorkspaceName() {
        return workspaceName;
    }

    @JsonProperty("workspace_name")
    public void setWorkspaceName(java.lang.String workspaceName) {
        this.workspaceName = workspaceName;
    }

    public ExtractBinAsAssemblyParams withWorkspaceName(java.lang.String workspaceName) {
        this.workspaceName = workspaceName;
        return this;
    }

    @JsonAnyGetter
    public Map<java.lang.String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    @JsonAnySetter
    public void setAdditionalProperties(java.lang.String name, Object value) {
        this.additionalProperties.put(name, value);
    }

    @Override
    public java.lang.String toString() {
        return ((((((((((((("ExtractBinAsAssemblyParams"+" [binnedContigObjRef=")+ binnedContigObjRef)+", extractedAssemblies=")+ extractedAssemblies)+", assemblySuffix=")+ assemblySuffix)+", assemblySetName=")+ assemblySetName)+", workspaceName=")+ workspaceName)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
