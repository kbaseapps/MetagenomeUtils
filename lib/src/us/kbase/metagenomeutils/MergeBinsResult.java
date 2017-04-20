
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
 * <p>Original spec-file type: MergeBinsResult</p>
 * <pre>
 * new_binned_contig_ref: newly created BinnedContig object referece
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "new_binned_contig_ref"
})
public class MergeBinsResult {

    @JsonProperty("new_binned_contig_ref")
    private String newBinnedContigRef;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("new_binned_contig_ref")
    public String getNewBinnedContigRef() {
        return newBinnedContigRef;
    }

    @JsonProperty("new_binned_contig_ref")
    public void setNewBinnedContigRef(String newBinnedContigRef) {
        this.newBinnedContigRef = newBinnedContigRef;
    }

    public MergeBinsResult withNewBinnedContigRef(String newBinnedContigRef) {
        this.newBinnedContigRef = newBinnedContigRef;
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
        return ((((("MergeBinsResult"+" [newBinnedContigRef=")+ newBinnedContigRef)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
