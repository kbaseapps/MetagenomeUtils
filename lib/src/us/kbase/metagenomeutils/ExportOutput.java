
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
 * <p>Original spec-file type: ExportOutput</p>
 * <pre>
 * shock_id: saved packed file shock id
 * bin_file_list: a list of bin file path
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "shock_id",
    "bin_file_list"
})
public class ExportOutput {

    @JsonProperty("shock_id")
    private java.lang.String shockId;
    @JsonProperty("bin_file_list")
    private List<String> binFileList;
    private Map<java.lang.String, Object> additionalProperties = new HashMap<java.lang.String, Object>();

    @JsonProperty("shock_id")
    public java.lang.String getShockId() {
        return shockId;
    }

    @JsonProperty("shock_id")
    public void setShockId(java.lang.String shockId) {
        this.shockId = shockId;
    }

    public ExportOutput withShockId(java.lang.String shockId) {
        this.shockId = shockId;
        return this;
    }

    @JsonProperty("bin_file_list")
    public List<String> getBinFileList() {
        return binFileList;
    }

    @JsonProperty("bin_file_list")
    public void setBinFileList(List<String> binFileList) {
        this.binFileList = binFileList;
    }

    public ExportOutput withBinFileList(List<String> binFileList) {
        this.binFileList = binFileList;
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
        return ((((((("ExportOutput"+" [shockId=")+ shockId)+", binFileList=")+ binFileList)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
