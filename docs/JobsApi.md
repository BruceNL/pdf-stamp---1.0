# swagger_client.JobsApi

All URIs are relative to *https://gw.api.cloud.sphereon.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_content**](JobsApi.md#add_content) | **POST** /jobs/{jobId}/streams/content | Upload a base64 encoded file
[**add_input_file**](JobsApi.md#add_input_file) | **POST** /jobs/{jobId}/streams/multipart | Upload a file
[**add_input_stream_locations**](JobsApi.md#add_input_stream_locations) | **POST** /jobs/{jobId}/streams/location | Add Input Stream Location(s)
[**create_job**](JobsApi.md#create_job) | **POST** /jobs | Create PDF stamper job
[**delete_job**](JobsApi.md#delete_job) | **DELETE** /jobs/{jobId} | Delete a job manually
[**get_first_stream**](JobsApi.md#get_first_stream) | **GET** /jobs/{jobId}/streams/result | Get the current/first result stream
[**get_job**](JobsApi.md#get_job) | **GET** /jobs/{jobId} | Job definition and state
[**get_jobs**](JobsApi.md#get_jobs) | **GET** /jobs | Get all jobs
[**get_stream_by_id**](JobsApi.md#get_stream_by_id) | **GET** /jobs/{jobId}/streams/result/{correlationId} | Get the result stream by correlation Id
[**submit_job**](JobsApi.md#submit_job) | **PUT** /jobs/{jobId} | Submit PDF stamper job for processing


# **add_content**
> PdfStamperJobResult add_content(content_request, job_id)

Upload a base64 encoded file

Upload an image, office or pdf for conversion to PDF, embedded in a json as a base64 encoded string

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobsApi()
content_request = swagger_client.ContentRequest() # ContentRequest | Content request
job_id = 'job_id_example' # str | jobId

try: 
    # Upload a base64 encoded file
    api_response = api_instance.add_content(content_request, job_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling JobsApi->add_content: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_request** | [**ContentRequest**](ContentRequest.md)| Content request | 
 **job_id** | **str**| jobId | 

### Return type

[**PdfStamperJobResult**](PdfStamperJobResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_input_file**
> PdfStamperJobResult add_input_file(job_id, stream)

Upload a file

Upload a pdf to stamp one or more configurations. Please note that you can upload multiple files.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobsApi()
job_id = 'job_id_example' # str | jobId
stream = '/path/to/file.txt' # file | The (additional) binary image or PDF (file/inputstream) to convert to PDF

try: 
    # Upload a file
    api_response = api_instance.add_input_file(job_id, stream)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling JobsApi->add_input_file: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| jobId | 
 **stream** | **file**| The (additional) binary image or PDF (file/inputstream) to convert to PDF | 

### Return type

[**PdfStamperJobResult**](PdfStamperJobResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_input_stream_locations**
> PdfStamperJobResult add_input_stream_locations(job_id, stream_locations)

Add Input Stream Location(s)

Add image, office or pdf input stream location(s) from the storage API for conversion to PDF. Please note that you can upload multiple files. Conversion will not be started yet.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobsApi()
job_id = 'job_id_example' # str | jobId
stream_locations = [swagger_client.InputResultLocation()] # list[InputResultLocation] | The (additional) binary image or PDF (file/inputstream) to convert to PDF

try: 
    # Add Input Stream Location(s)
    api_response = api_instance.add_input_stream_locations(job_id, stream_locations)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling JobsApi->add_input_stream_locations: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| jobId | 
 **stream_locations** | [**list[InputResultLocation]**](InputResultLocation.md)| The (additional) binary image or PDF (file/inputstream) to convert to PDF | 

### Return type

[**PdfStamperJobResult**](PdfStamperJobResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_job**
> PdfStamperJobResult create_job(job_request)

Create PDF stamper job

Create a job using the given settings.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobsApi()
job_request = swagger_client.PdfStamperJobRequest() # PdfStamperJobRequest | jobRequest

try: 
    # Create PDF stamper job
    api_response = api_instance.create_job(job_request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling JobsApi->create_job: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_request** | [**PdfStamperJobRequest**](PdfStamperJobRequest.md)| jobRequest | 

### Return type

[**PdfStamperJobResult**](PdfStamperJobResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_job**
> PdfStamperJobResult delete_job(job_id)

Delete a job manually

Delete the PDF stamper job and all related files depending on the lifecycle.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobsApi()
job_id = 'job_id_example' # str | jobId

try: 
    # Delete a job manually
    api_response = api_instance.delete_job(job_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling JobsApi->delete_job: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| jobId | 

### Return type

[**PdfStamperJobResult**](PdfStamperJobResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_first_stream**
> str get_first_stream(job_id)

Get the current/first result stream

Get the PDF stamper as binary stream/file.  Our API generation does not allow changing the media type based on the Accepted header unfortunately.  This means we use a separate path postfix with the value '/stream'.  This API only returns the PDF when the response status is DONE.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobsApi()
job_id = 'job_id_example' # str | jobId

try: 
    # Get the current/first result stream
    api_response = api_instance.get_first_stream(job_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling JobsApi->get_first_stream: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| jobId | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job**
> PdfStamperJobResult get_job(job_id)

Job definition and state

Get the PDF stamper job definition and current state. Please note that you can differentiate based on http response status.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobsApi()
job_id = 'job_id_example' # str | jobId

try: 
    # Job definition and state
    api_response = api_instance.get_job(job_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling JobsApi->get_job: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| jobId | 

### Return type

[**PdfStamperJobResult**](PdfStamperJobResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jobs**
> list[PdfStamperJobResult] get_jobs(job_statuses=job_statuses)

Get all jobs

Get all PDF stamper job definitions and their current state.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobsApi()
job_statuses = ['job_statuses_example'] # list[str] | A list of jobStatuses to filter on. (optional)

try: 
    # Get all jobs
    api_response = api_instance.get_jobs(job_statuses=job_statuses)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling JobsApi->get_jobs: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_statuses** | [**list[str]**](str.md)| A list of jobStatuses to filter on. | [optional] 

### Return type

[**list[PdfStamperJobResult]**](PdfStamperJobResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stream_by_id**
> str get_stream_by_id(correlation_id, job_id)

Get the result stream by correlation Id

Get the PDF stamper as binary stream/file by correlation Id.  Our API generation does not allow changing the media type based on the Accepted header unfortunately.  This means we use a separate path postfix with the value '/stream'.  This API only returns the PDF when the response status is DONE.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobsApi()
correlation_id = 'correlation_id_example' # str | correlationId
job_id = 'job_id_example' # str | jobId

try: 
    # Get the result stream by correlation Id
    api_response = api_instance.get_stream_by_id(correlation_id, job_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling JobsApi->get_stream_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **correlation_id** | **str**| correlationId | 
 **job_id** | **str**| jobId | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_job**
> PdfStamperJobResult submit_job(job_id)

Submit PDF stamper job for processing

Start PDF stamper job for processing. Stamp one or more configurations on the previously uploaded PDFs. If the optional settings are supplied with the job in the request body, they are being used, otherwise the settings created during job creation are being used. You can only submit the job after a new Job is created with status INPUTS_UPLOADED or resubmit an existing Job with status ERROR.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobsApi()
job_id = 'job_id_example' # str | jobId

try: 
    # Submit PDF stamper job for processing
    api_response = api_instance.submit_job(job_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling JobsApi->submit_job: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| jobId | 

### Return type

[**PdfStamperJobResult**](PdfStamperJobResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

