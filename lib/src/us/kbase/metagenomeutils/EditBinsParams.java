
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
 * <p>Original spec-file type: EditBinsParams</p>
 * <pre>
 * old_binned_contig_ref: Original BinnedContig object reference
 * bins_to_remove: a list of bin ids to be removed
 * bin_merges: a list of bin merges dicts
 *   new_bin_id: newly created bin id
 *   bin_to_merge: list of bins to merge
 * output_binned_contig_name: Name for the output BinnedContigs object
 * workspace_name: the name of the workspace new object gets saved to
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "old_binned_contig_ref",
    "bins_to_remove",
    "bin_merges",
    "output_binned_contig_name",
    "workspace_name"
})
public class EditBinsParams {

    @JsonProperty("old_binned_contig_ref")
    private java.lang.String oldBinnedContigRef;
    @JsonProperty("bins_to_remove")
    private List<String> binsToRemove;
    @JsonProperty("bin_merges")
    private List<Map<String, String>> binMerges;
    @JsonProperty("output_binned_contig_name")
    private java.lang.String outputBinnedContigName;
    @JsonProperty("workspace_name")
    private java.lang.String workspaceName;
    private Map<java.lang.String, Object> additionalProperties = new HashMap<java.lang.String, Object>();

    @JsonProperty("old_binned_contig_ref")
    public java.lang.String getOldBinnedContigRef() {
        return oldBinnedContigRef;
    }

    @JsonProperty("old_binned_contig_ref")
    public void setOldBinnedContigRef(java.lang.String oldBinnedContigRef) {
        this.oldBinnedContigRef = oldBinnedContigRef;
    }

    public EditBinsParams withOldBinnedContigRef(java.lang.String oldBinnedContigRef) {
        this.oldBinnedContigRef = oldBinnedContigRef;
        return this;
    }

    @JsonProperty("bins_to_remove")
    public List<String> getBinsToRemove() {
        return binsToRemove;
    }

    @JsonProperty("bins_to_remove")
    public void setBinsToRemove(List<String> binsToRemove) {
        this.binsToRemove = binsToRemove;
    }

    public EditBinsParams withBinsToRemove(List<String> binsToRemove) {
        this.binsToRemove = binsToRemove;
        return this;
    }

    @JsonProperty("bin_merges")
    public List<Map<String, String>> getBinMerges() {
        return binMerges;
    }

    @JsonProperty("bin_merges")
    public void setBinMerges(List<Map<String, String>> binMerges) {
        this.binMerges = binMerges;
    }

    public EditBinsParams withBinMerges(List<Map<String, String>> binMerges) {
        this.binMerges = binMerges;
        return this;
    }

    @JsonProperty("output_binned_contig_name")
    public java.lang.String getOutputBinnedContigName() {
        return outputBinnedContigName;
    }

    @JsonProperty("output_binned_contig_name")
    public void setOutputBinnedContigName(java.lang.String outputBinnedContigName) {
        this.outputBinnedContigName = outputBinnedContigName;
    }

    public EditBinsParams withOutputBinnedContigName(java.lang.String outputBinnedContigName) {
        this.outputBinnedContigName = outputBinnedContigName;
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

    public EditBinsParams withWorkspaceName(java.lang.String workspaceName) {
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
        return ((((((((((((("EditBinsParams"+" [oldBinnedContigRef=")+ oldBinnedContigRef)+", binsToRemove=")+ binsToRemove)+", binMerges=")+ binMerges)+", outputBinnedContigName=")+ outputBinnedContigName)+", workspaceName=")+ workspaceName)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
