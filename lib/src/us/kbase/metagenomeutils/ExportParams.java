
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
 * <p>Original spec-file type: ExportParams</p>
 * <pre>
 * input_ref: BinnedContig object reference
 * optional params:
 * not_save_to_shock: not saving result bin files to shock
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "input_ref",
    "not_save_to_shock"
})
public class ExportParams {

    @JsonProperty("input_ref")
    private String inputRef;
    @JsonProperty("not_save_to_shock")
    private Long notSaveToShock;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("input_ref")
    public String getInputRef() {
        return inputRef;
    }

    @JsonProperty("input_ref")
    public void setInputRef(String inputRef) {
        this.inputRef = inputRef;
    }

    public ExportParams withInputRef(String inputRef) {
        this.inputRef = inputRef;
        return this;
    }

    @JsonProperty("not_save_to_shock")
    public Long getNotSaveToShock() {
        return notSaveToShock;
    }

    @JsonProperty("not_save_to_shock")
    public void setNotSaveToShock(Long notSaveToShock) {
        this.notSaveToShock = notSaveToShock;
    }

    public ExportParams withNotSaveToShock(Long notSaveToShock) {
        this.notSaveToShock = notSaveToShock;
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
        return ((((((("ExportParams"+" [inputRef=")+ inputRef)+", notSaveToShock=")+ notSaveToShock)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
