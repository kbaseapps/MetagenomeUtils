
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
 * <p>Original spec-file type: ExportOutput</p>
 * <pre>
 * shock_id: saved packed file shock id
 * bin_file_directory: directory that contains all bin files
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "shock_id",
    "bin_file_directory"
})
public class ExportOutput {

    @JsonProperty("shock_id")
    private String shockId;
    @JsonProperty("bin_file_directory")
    private String binFileDirectory;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("shock_id")
    public String getShockId() {
        return shockId;
    }

    @JsonProperty("shock_id")
    public void setShockId(String shockId) {
        this.shockId = shockId;
    }

    public ExportOutput withShockId(String shockId) {
        this.shockId = shockId;
        return this;
    }

    @JsonProperty("bin_file_directory")
    public String getBinFileDirectory() {
        return binFileDirectory;
    }

    @JsonProperty("bin_file_directory")
    public void setBinFileDirectory(String binFileDirectory) {
        this.binFileDirectory = binFileDirectory;
    }

    public ExportOutput withBinFileDirectory(String binFileDirectory) {
        this.binFileDirectory = binFileDirectory;
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
        return ((((((("ExportOutput"+" [shockId=")+ shockId)+", binFileDirectory=")+ binFileDirectory)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
