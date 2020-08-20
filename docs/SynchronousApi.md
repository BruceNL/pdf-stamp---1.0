# swagger_client.SynchronousApi

All URIs are relative to *https://gw.api.cloud.sphereon.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sync_job_content**](SynchronousApi.md#sync_job_content) | **POST** /sync/streams/content | Execute a synchronous stamp job with a content request/response.
[**sync_job_stream_location**](SynchronousApi.md#sync_job_stream_location) | **POST** /sync/streams/location | Execute a synchronous stamp job with a streamlocation.


# **sync_job_content**
> ContentResponse sync_job_content(content_request)

Execute a synchronous stamp job with a content request/response.

Execute a synchronous stamp job using the given configId. Header parameters will be parsed for additional template variables.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SynchronousApi()
content_request = swagger_client.ContentRequest() # ContentRequest | File content

try: 
    # Execute a synchronous stamp job with a content request/response.
    api_response = api_instance.sync_job_content(content_request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SynchronousApi->sync_job_content: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_request** | [**ContentRequest**](ContentRequest.md)| File content | 

### Return type

[**ContentResponse**](ContentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_job_stream_location**
> PdfStamperJobResult sync_job_stream_location(job_request)

Execute a synchronous stamp job with a streamlocation.

Execute a synchronous stamp job using the given configId. Header parameters will be parsed for additional template variables.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SynchronousApi()
job_request = swagger_client.PdfStamperJobRequest() # PdfStamperJobRequest | Job request

try: 
    # Execute a synchronous stamp job with a streamlocation.
    api_response = api_instance.sync_job_stream_location(job_request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SynchronousApi->sync_job_stream_location: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_request** | [**PdfStamperJobRequest**](PdfStamperJobRequest.md)| Job request | 

### Return type

[**PdfStamperJobResult**](PdfStamperJobResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

