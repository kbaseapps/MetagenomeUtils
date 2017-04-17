
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
 * extracted_assemblies: a list of:
 *       bin_id: target bin id to be extracted
 *       output_assembly_name: output assembly object name
 * workspace_name: the name of the workspace it gets saved to
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "binned_contig_obj_ref",
    "bin_id",
    "output_assembly_name",
    "extracted_assemblies",
    "workspace_name"
})
public class ExtractBinAsAssemblyParams {

    @JsonProperty("binned_contig_obj_ref")
    private java.lang.String binnedContigObjRef;
    @JsonProperty("bin_id")
    private java.lang.String binId;
    @JsonProperty("output_assembly_name")
    private java.lang.String outputAssemblyName;
    @JsonProperty("extracted_assemblies")
    private List<Map<String, String>> extractedAssemblies;
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

    @JsonProperty("bin_id")
    public java.lang.String getBinId() {
        return binId;
    }

    @JsonProperty("bin_id")
    public void setBinId(java.lang.String binId) {
        this.binId = binId;
    }

    public ExtractBinAsAssemblyParams withBinId(java.lang.String binId) {
        this.binId = binId;
        return this;
    }

    @JsonProperty("output_assembly_name")
    public java.lang.String getOutputAssemblyName() {
        return outputAssemblyName;
    }

    @JsonProperty("output_assembly_name")
    public void setOutputAssemblyName(java.lang.String outputAssemblyName) {
        this.outputAssemblyName = outputAssemblyName;
    }

    public ExtractBinAsAssemblyParams withOutputAssemblyName(java.lang.String outputAssemblyName) {
        this.outputAssemblyName = outputAssemblyName;
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
        return ((((((((((((("ExtractBinAsAssemblyParams"+" [binnedContigObjRef=")+ binnedContigObjRef)+", binId=")+ binId)+", outputAssemblyName=")+ outputAssemblyName)+", extractedAssemblies=")+ extractedAssemblies)+", workspaceName=")+ workspaceName)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
