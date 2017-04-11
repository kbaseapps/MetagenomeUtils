
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
 * <p>Original spec-file type: FileToBinnedContigResult</p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "binned_contig_obj_ref"
})
public class FileToBinnedContigResult {

    @JsonProperty("binned_contig_obj_ref")
    private String binnedContigObjRef;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("binned_contig_obj_ref")
    public String getBinnedContigObjRef() {
        return binnedContigObjRef;
    }

    @JsonProperty("binned_contig_obj_ref")
    public void setBinnedContigObjRef(String binnedContigObjRef) {
        this.binnedContigObjRef = binnedContigObjRef;
    }

    public FileToBinnedContigResult withBinnedContigObjRef(String binnedContigObjRef) {
        this.binnedContigObjRef = binnedContigObjRef;
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
        return ((((("FileToBinnedContigResult"+" [binnedContigObjRef=")+ binnedContigObjRef)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
