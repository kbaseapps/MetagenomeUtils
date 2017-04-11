
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
 * <p>Original spec-file type: FileToBinnedContigParams</p>
 * <pre>
 * file_directory: file directory containing compressed/unpacked contig file(s) to build BinnedContig object
 * assembly_ref: Metagenome assembly object reference
 * binned_contig_name: BinnedContig object name
 * workspace_name: the name/id of the workspace it gets saved to
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "file_directory",
    "assembly_ref",
    "binned_contig_name",
    "workspace_name"
})
public class FileToBinnedContigParams {

    @JsonProperty("file_directory")
    private String fileDirectory;
    @JsonProperty("assembly_ref")
    private String assemblyRef;
    @JsonProperty("binned_contig_name")
    private String binnedContigName;
    @JsonProperty("workspace_name")
    private String workspaceName;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("file_directory")
    public String getFileDirectory() {
        return fileDirectory;
    }

    @JsonProperty("file_directory")
    public void setFileDirectory(String fileDirectory) {
        this.fileDirectory = fileDirectory;
    }

    public FileToBinnedContigParams withFileDirectory(String fileDirectory) {
        this.fileDirectory = fileDirectory;
        return this;
    }

    @JsonProperty("assembly_ref")
    public String getAssemblyRef() {
        return assemblyRef;
    }

    @JsonProperty("assembly_ref")
    public void setAssemblyRef(String assemblyRef) {
        this.assemblyRef = assemblyRef;
    }

    public FileToBinnedContigParams withAssemblyRef(String assemblyRef) {
        this.assemblyRef = assemblyRef;
        return this;
    }

    @JsonProperty("binned_contig_name")
    public String getBinnedContigName() {
        return binnedContigName;
    }

    @JsonProperty("binned_contig_name")
    public void setBinnedContigName(String binnedContigName) {
        this.binnedContigName = binnedContigName;
    }

    public FileToBinnedContigParams withBinnedContigName(String binnedContigName) {
        this.binnedContigName = binnedContigName;
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

    public FileToBinnedContigParams withWorkspaceName(String workspaceName) {
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
        return ((((((((((("FileToBinnedContigParams"+" [fileDirectory=")+ fileDirectory)+", assemblyRef=")+ assemblyRef)+", binnedContigName=")+ binnedContigName)+", workspaceName=")+ workspaceName)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
