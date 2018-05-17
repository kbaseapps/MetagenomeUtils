
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
 * <p>Original spec-file type: ImportExcelParams</p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "shock_id",
    "workspace_name",
    "binned_contigs_name"
})
public class ImportExcelParams {

    @JsonProperty("shock_id")
    private String shockId;
    @JsonProperty("workspace_name")
    private String workspaceName;
    @JsonProperty("binned_contigs_name")
    private String binnedContigsName;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("shock_id")
    public String getShockId() {
        return shockId;
    }

    @JsonProperty("shock_id")
    public void setShockId(String shockId) {
        this.shockId = shockId;
    }

    public ImportExcelParams withShockId(String shockId) {
        this.shockId = shockId;
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

    public ImportExcelParams withWorkspaceName(String workspaceName) {
        this.workspaceName = workspaceName;
        return this;
    }

    @JsonProperty("binned_contigs_name")
    public String getBinnedContigsName() {
        return binnedContigsName;
    }

    @JsonProperty("binned_contigs_name")
    public void setBinnedContigsName(String binnedContigsName) {
        this.binnedContigsName = binnedContigsName;
    }

    public ImportExcelParams withBinnedContigsName(String binnedContigsName) {
        this.binnedContigsName = binnedContigsName;
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
        return ((((((((("ImportExcelParams"+" [shockId=")+ shockId)+", workspaceName=")+ workspaceName)+", binnedContigsName=")+ binnedContigsName)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
