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
     * save_to_shock: saving result bin files to shock. default to True
     * return params:
     * shock_id: saved packed file shock id (None if save_to_shock is set to False)
     * bin_file_directory: directory that contains all bin files
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

    /**
     * <p>Original spec-file function name: remove_bins_from_binned_contig</p>
     * <pre>
     * remove_bins_from_binned_contig: remove a list of bins from BinnedContig object
     * input params:
     * old_binned_contig_ref: Original BinnedContig object reference
     * bins_to_remove: a list of bin ids to be removed
     * output_binned_contig_name: Name for the output BinnedContigs object
     * workspace_name: the name of the workspace new object gets saved to
     * return params:
     * new_binned_contig_ref: newly created BinnedContig object referece
     * </pre>
     * @param   params   instance of type {@link us.kbase.metagenomeutils.RemoveBinsParams RemoveBinsParams}
     * @return   parameter "returnVal" of type {@link us.kbase.metagenomeutils.RemoveBinsResult RemoveBinsResult}
     * @throws IOException if an IO exception occurs
     * @throws JsonClientException if a JSON RPC exception occurs
     */
    public RemoveBinsResult removeBinsFromBinnedContig(RemoveBinsParams params, RpcContext... jsonRpcContext) throws IOException, JsonClientException {
        List<Object> args = new ArrayList<Object>();
        args.add(params);
        TypeReference<List<RemoveBinsResult>> retType = new TypeReference<List<RemoveBinsResult>>() {};
        List<RemoveBinsResult> res = caller.jsonrpcCall("MetagenomeUtils.remove_bins_from_binned_contig", args, retType, true, true, jsonRpcContext, this.serviceVersion);
        return res.get(0);
    }

    /**
     * <p>Original spec-file function name: merge_bins_from_binned_contig</p>
     * <pre>
     * merge_bins_from_binned_contig: merge a list of bins from BinnedContig object
     * input params:
     * old_binned_contig_ref: Original BinnedContig object reference
     * bin_merges: a list of bin merges dicts
     *   new_bin_id: newly created bin id
     *   bin_to_merge: list of bins to merge
     * output_binned_contig_name: Name for the output BinnedContigs object
     * workspace_name: the name of the workspace new object gets saved to
     * return params:
     * new_binned_contig_ref: newly created BinnedContig object referece
     * </pre>
     * @param   params   instance of type {@link us.kbase.metagenomeutils.MergeBinsParams MergeBinsParams}
     * @return   parameter "returnVal" of type {@link us.kbase.metagenomeutils.MergeBinsResult MergeBinsResult}
     * @throws IOException if an IO exception occurs
     * @throws JsonClientException if a JSON RPC exception occurs
     */
    public MergeBinsResult mergeBinsFromBinnedContig(MergeBinsParams params, RpcContext... jsonRpcContext) throws IOException, JsonClientException {
        List<Object> args = new ArrayList<Object>();
        args.add(params);
        TypeReference<List<MergeBinsResult>> retType = new TypeReference<List<MergeBinsResult>>() {};
        List<MergeBinsResult> res = caller.jsonrpcCall("MetagenomeUtils.merge_bins_from_binned_contig", args, retType, true, true, jsonRpcContext, this.serviceVersion);
        return res.get(0);
    }

    /**
     * <p>Original spec-file function name: edit_bins_from_binned_contig</p>
     * <pre>
     * edit_bins_from_binned_contig: merge/remove a list of bins from BinnedContig object
     *                               a wrapper method of:
     *                               merge_bins_from_binned_contig
     *                               remove_bins_from_binned_contig
     * input params:
     * old_binned_contig_ref: Original BinnedContig object reference
     * bins_to_remove: a list of bin ids to be removed
     * bin_merges: a list of bin merges dicts
     *   new_bin_id: newly created bin id
     *   bin_to_merge: list of bins to merge
     * output_binned_contig_name: Name for the output BinnedContigs object
     * workspace_name: the name of the workspace new object gets saved to
     * return params:
     * new_binned_contig_ref: newly created BinnedContig object referece
     * report_name: report name generated by KBaseReport
     * report_ref: report reference generated by KBaseReport
     * </pre>
     * @param   params   instance of type {@link us.kbase.metagenomeutils.EditBinsParams EditBinsParams}
     * @return   parameter "returnVal" of type {@link us.kbase.metagenomeutils.EditBinsResult EditBinsResult}
     * @throws IOException if an IO exception occurs
     * @throws JsonClientException if a JSON RPC exception occurs
     */
    public EditBinsResult editBinsFromBinnedContig(EditBinsParams params, RpcContext... jsonRpcContext) throws IOException, JsonClientException {
        List<Object> args = new ArrayList<Object>();
        args.add(params);
        TypeReference<List<EditBinsResult>> retType = new TypeReference<List<EditBinsResult>>() {};
        List<EditBinsResult> res = caller.jsonrpcCall("MetagenomeUtils.edit_bins_from_binned_contig", args, retType, true, true, jsonRpcContext, this.serviceVersion);
        return res.get(0);
    }

    public Map<String, Object> status(RpcContext... jsonRpcContext) throws IOException, JsonClientException {
        List<Object> args = new ArrayList<Object>();
        TypeReference<List<Map<String, Object>>> retType = new TypeReference<List<Map<String, Object>>>() {};
        List<Map<String, Object>> res = caller.jsonrpcCall("MetagenomeUtils.status", args, retType, true, false, jsonRpcContext, this.serviceVersion);
        return res.get(0);
    }
}
