
package us.kbase.metagenomeutils;

import java.util.HashMap;
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
    private String binnedContigObjRef;
    @JsonProperty("extracted_assemblies")
    private String extractedAssemblies;
    @JsonProperty("assembly_suffix")
    private String assemblySuffix;
    @JsonProperty("assembly_set_name")
    private String assemblySetName;
    @JsonProperty("workspace_name")
    private String workspaceName;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("binned_contig_obj_ref")
    public String getBinnedContigObjRef() {
        return binnedContigObjRef;
    }

    @JsonProperty("binned_contig_obj_ref")
    public void setBinnedContigObjRef(String binnedContigObjRef) {
        this.binnedContigObjRef = binnedContigObjRef;
    }

    public ExtractBinAsAssemblyParams withBinnedContigObjRef(String binnedContigObjRef) {
        this.binnedContigObjRef = binnedContigObjRef;
        return this;
    }

    @JsonProperty("extracted_assemblies")
    public String getExtractedAssemblies() {
        return extractedAssemblies;
    }

    @JsonProperty("extracted_assemblies")
    public void setExtractedAssemblies(String extractedAssemblies) {
        this.extractedAssemblies = extractedAssemblies;
    }

    public ExtractBinAsAssemblyParams withExtractedAssemblies(String extractedAssemblies) {
        this.extractedAssemblies = extractedAssemblies;
        return this;
    }

    @JsonProperty("assembly_suffix")
    public String getAssemblySuffix() {
        return assemblySuffix;
    }

    @JsonProperty("assembly_suffix")
    public void setAssemblySuffix(String assemblySuffix) {
        this.assemblySuffix = assemblySuffix;
    }

    public ExtractBinAsAssemblyParams withAssemblySuffix(String assemblySuffix) {
        this.assemblySuffix = assemblySuffix;
        return this;
    }

    @JsonProperty("assembly_set_name")
    public String getAssemblySetName() {
        return assemblySetName;
    }

    @JsonProperty("assembly_set_name")
    public void setAssemblySetName(String assemblySetName) {
        this.assemblySetName = assemblySetName;
    }

    public ExtractBinAsAssemblyParams withAssemblySetName(String assemblySetName) {
        this.assemblySetName = assemblySetName;
        return this;
    }

    @JsonProperty("workspace_name")
    public String getWorkspaceName() {
        return workspaceName;
    }

    @JsonProperty("workspace_name")
    public void setWorkspaceName(String workspaceName) {
        this.workspaceName = workspaceName;
    }

    public ExtractBinAsAssemblyParams withWorkspaceName(String workspaceName) {
        this.workspaceName = workspaceName;
        return this;
    }

    @JsonAnyGetter
    public Map<String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    @JsonAnySetter
    public void setAdditionalProperties(String name, Object value) {
        this.additionalProperties.put(name, value);
    }

    @Override
    public String toString() {
        return ((((((((((((("ExtractBinAsAssemblyParams"+" [binnedContigObjRef=")+ binnedContigObjRef)+", extractedAssemblies=")+ extractedAssemblies)+", assemblySuffix=")+ assemblySuffix)+", assemblySetName=")+ assemblySetName)+", workspaceName=")+ workspaceName)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
