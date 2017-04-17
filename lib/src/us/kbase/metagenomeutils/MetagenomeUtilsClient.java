package us.kbase.metagenomeutils;

import com.fasterxml.jackson.core.type.TypeReference;
import java.io.File;
import java.io.IOException;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import us.kbase.auth.AuthToken;
import us.kbase.common.service.JsonClientCaller;
import us.kbase.common.service.JsonClientException;
import us.kbase.common.service.RpcContext;
import us.kbase.common.service.UnauthorizedException;

/**
 * <p>Original spec-file module name: MetagenomeUtils</p>
 * <pre>
 * A KBase module for interacting with Metagenomic data in KBase
 * </pre>
 */
public class MetagenomeUtilsClient {
    private JsonClientCaller caller;
    private String serviceVersion = null;


    /** Constructs a client with a custom URL and no user credentials.
     * @param url the URL of the service.
     */
    public MetagenomeUtilsClient(URL url) {
        caller = new JsonClientCaller(url);
    }
    /** Constructs a client with a custom URL.
     * @param url the URL of the service.
     * @param token the user's authorization token.
     * @throws UnauthorizedException if the token is not valid.
     * @throws IOException if an IOException occurs when checking the token's
     * validity.
     */
    public MetagenomeUtilsClient(URL url, AuthToken token) throws UnauthorizedException, IOException {
        caller = new JsonClientCaller(url, token);
    }

    /** Constructs a client with a custom URL.
     * @param url the URL of the service.
     * @param user the user name.
     * @param password the password for the user name.
     * @throws UnauthorizedException if the credentials are not valid.
     * @throws IOException if an IOException occurs when checking the user's
     * credentials.
     */
    public MetagenomeUtilsClient(URL url, String user, String password) throws UnauthorizedException, IOException {
        caller = new JsonClientCaller(url, user, password);
    }

    /** Constructs a client with a custom URL
     * and a custom authorization service URL.
     * @param url the URL of the service.
     * @param user the user name.
     * @param password the password for the user name.
     * @param auth the URL of the authorization server.
     * @throws UnauthorizedException if the credentials are not valid.
     * @throws IOException if an IOException occurs when checking the user's
     * credentials.
     */
    public MetagenomeUtilsClient(URL url, String user, String password, URL auth) throws UnauthorizedException, IOException {
        caller = new JsonClientCaller(url, user, password, auth);
    }

    /** Get the token this client uses to communicate with the server.
     * @return the authorization token.
     */
    public AuthToken getToken() {
        return caller.getToken();
    }

    /** Get the URL of the service with which this client communicates.
     * @return the service URL.
     */
    public URL getURL() {
        return caller.getURL();
    }

    /** Set the timeout between establishing a connection to a server and
     * receiving a response. A value of zero or null implies no timeout.
     * @param milliseconds the milliseconds to wait before timing out when
     * attempting to read from a server.
     */
    public void setConnectionReadTimeOut(Integer milliseconds) {
        this.caller.setConnectionReadTimeOut(milliseconds);
    }

    /** Check if this client allows insecure http (vs https) connections.
     * @return true if insecure connections are allowed.
     */
    public boolean isInsecureHttpConnectionAllowed() {
        return caller.isInsecureHttpConnectionAllowed();
    }

    /** Deprecated. Use isInsecureHttpConnectionAllowed().
     * @deprecated
     */
    public boolean isAuthAllowedForHttp() {
        return caller.isAuthAllowedForHttp();
    }

    /** Set whether insecure http (vs https) connections should be allowed by
     * this client.
     * @param allowed true to allow insecure connections. Default false
     */
    public void setIsInsecureHttpConnectionAllowed(boolean allowed) {
        caller.setInsecureHttpConnectionAllowed(allowed);
    }

    /** Deprecated. Use setIsInsecureHttpConnectionAllowed().
     * @deprecated
     */
    public void setAuthAllowedForHttp(boolean isAuthAllowedForHttp) {
        caller.setAuthAllowedForHttp(isAuthAllowedForHttp);
    }

    /** Set whether all SSL certificates, including self-signed certificates,
     * should be trusted.
     * @param trustAll true to trust all certificates. Default false.
     */
    public void setAllSSLCertificatesTrusted(final boolean trustAll) {
        caller.setAllSSLCertificatesTrusted(trustAll);
    }
    
    /** Check if this client trusts all SSL certificates, including
     * self-signed certificates.
     * @return true if all certificates are trusted.
     */
    public boolean isAllSSLCertificatesTrusted() {
        return caller.isAllSSLCertificatesTrusted();
    }
    /** Sets streaming mode on. In this case, the data will be streamed to
     * the server in chunks as it is read from disk rather than buffered in
     * memory. Many servers are not compatible with this feature.
     * @param streamRequest true to set streaming mode on, false otherwise.
     */
    public void setStreamingModeOn(boolean streamRequest) {
        caller.setStreamingModeOn(streamRequest);
    }

    /** Returns true if streaming mode is on.
     * @return true if streaming mode is on.
     */
    public boolean isStreamingModeOn() {
        return caller.isStreamingModeOn();
    }

    public void _setFileForNextRpcResponse(File f) {
        caller.setFileForNextRpcResponse(f);
    }

    public String getServiceVersion() {
        return this.serviceVersion;
    }

    public void setServiceVersion(String newValue) {
        this.serviceVersion = newValue;
    }

    /**
     * <p>Original spec-file function name: file_to_binned_contigs</p>
     * <pre>
     * file_to_binned_contigs: Generating BinnedContigs ojbect from files
     * input params:
     * file_directory: file directory containing compressed/unpacked contig file(s) to build BinnedContig object
     * assembly_ref: Metagenome assembly object reference
     * binned_contig_name: BinnedContig object name
     * workspace_name: the name/id of the workspace it gets saved to
     * return params:
     * binned_contig_obj_ref: generated result BinnedContig object reference
     * </pre>
     * @param   params   instance of type {@link us.kbase.metagenomeutils.FileToBinnedContigParams FileToBinnedContigParams}
     * @return   parameter "returnVal" of type {@link us.kbase.metagenomeutils.FileToBinnedContigResult FileToBinnedContigResult}
     * @throws IOException if an IO exception occurs
     * @throws JsonClientException if a JSON RPC exception occurs
     */
    public FileToBinnedContigResult fileToBinnedContigs(FileToBinnedContigParams params, RpcContext... jsonRpcContext) throws IOException, JsonClientException {
        List<Object> args = new ArrayList<Object>();
        args.add(params);
        TypeReference<List<FileToBinnedContigResult>> retType = new TypeReference<List<FileToBinnedContigResult>>() {};
        List<FileToBinnedContigResult> res = caller.jsonrpcCall("MetagenomeUtils.file_to_binned_contigs", args, retType, true, true, jsonRpcContext, this.serviceVersion);
        return res.get(0);
    }

    /**
     * <p>Original spec-file function name: binned_contigs_to_file</p>
     * <pre>
     * binned_contigs_to_file: Convert BinnedContig object to fasta files and pack them to shock
     * required params:
     * input_ref: BinnedContig object reference
     * optional params:
     * not_save_to_shock: not saving result bin files to shock
     * return params:
     * shock_id: saved packed file shock id (None if not_save_to_shock is set)
     * bin_file_list: a list of bin file path
     * </pre>
     * @param   params   instance of type {@link us.kbase.metagenomeutils.ExportParams ExportParams}
     * @return   parameter "returnVal" of type {@link us.kbase.metagenomeutils.ExportOutput ExportOutput}
     * @throws IOException if an IO exception occurs
     * @throws JsonClientException if a JSON RPC exception occurs
     */
    public ExportOutput binnedContigsToFile(ExportParams params, RpcContext... jsonRpcContext) throws IOException, JsonClientException {
        List<Object> args = new ArrayList<Object>();
        args.add(params);
        TypeReference<List<ExportOutput>> retType = new TypeReference<List<ExportOutput>>() {};
        List<ExportOutput> res = caller.jsonrpcCall("MetagenomeUtils.binned_contigs_to_file", args, retType, true, true, jsonRpcContext, this.serviceVersion);
        return res.get(0);
    }

    /**
     * <p>Original spec-file function name: extract_binned_contigs_as_assembly</p>
     * <pre>
     * extract_binned_contigs_as_assembly: extract one/multiple Bins from BinnedContigs as Assembly object
     * input params:
     * binned_contig_obj_ref: BinnedContig object reference
     * extracted_assemblies: a list of:
     *       bin_id: target bin id to be extracted
     *       output_assembly_name: output assembly object name
     * workspace_name: the name of the workspace it gets saved to
     * return params:
     * assembly_ref_list: list of generated result Assembly object reference
     * report_name: report name generated by KBaseReport
     * report_ref: report reference generated by KBaseReport
     * </pre>
     * @param   params   instance of type {@link us.kbase.metagenomeutils.ExtractBinAsAssemblyParams ExtractBinAsAssemblyParams}
     * @return   parameter "returnVal" of type {@link us.kbase.metagenomeutils.ExtractBinAsAssemblyResult ExtractBinAsAssemblyResult}
     * @throws IOException if an IO exception occurs
     * @throws JsonClientException if a JSON RPC exception occurs
     */
    public ExtractBinAsAssemblyResult extractBinnedContigsAsAssembly(ExtractBinAsAssemblyParams params, RpcContext... jsonRpcContext) throws IOException, JsonClientException {
        List<Object> args = new ArrayList<Object>();
        args.add(params);
        TypeReference<List<ExtractBinAsAssemblyResult>> retType = new TypeReference<List<ExtractBinAsAssemblyResult>>() {};
        List<ExtractBinAsAssemblyResult> res = caller.jsonrpcCall("MetagenomeUtils.extract_binned_contigs_as_assembly", args, retType, true, true, jsonRpcContext, this.serviceVersion);
        return res.get(0);
    }

    public Map<String, Object> status(RpcContext... jsonRpcContext) throws IOException, JsonClientException {
        List<Object> args = new ArrayList<Object>();
        TypeReference<List<Map<String, Object>>> retType = new TypeReference<List<Map<String, Object>>>() {};
        List<Map<String, Object>> res = caller.jsonrpcCall("MetagenomeUtils.status", args, retType, true, false, jsonRpcContext, this.serviceVersion);
        return res.get(0);
    }
}
