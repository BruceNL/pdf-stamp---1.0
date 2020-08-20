# swagger_client.ConfigApi

All URIs are relative to *https://gw.api.cloud.sphereon.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_configuration**](ConfigApi.md#create_configuration) | **POST** /config | Create PDF stamper configuration
[**delete_configuration**](ConfigApi.md#delete_configuration) | **DELETE** /config/{configId} | Delete PDF stamper configuration
[**delete_resources**](ConfigApi.md#delete_resources) | **DELETE** /config/{configId}/streams | Delete resources
[**get_configuration**](ConfigApi.md#get_configuration) | **GET** /config/{configId} | Get PDF stamper configuration
[**update_configuration**](ConfigApi.md#update_configuration) | **PUT** /config/{configId} | Update PDF stamper configuration
[**upload_resource**](ConfigApi.md#upload_resource) | **POST** /config/{configId}/streams/multipart | Upload a configuration resource


# **create_configuration**
> StamperConfigResponse create_configuration(stamp_configuration)

Create PDF stamper configuration

Create / initialize a new PDF stamper configuration.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigApi()
stamp_configuration = swagger_client.StamperConfig() # StamperConfig | The PDF stamper configuration

try: 
    # Create PDF stamper configuration
    api_response = api_instance.create_configuration(stamp_configuration)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConfigApi->create_configuration: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stamp_configuration** | [**StamperConfig**](StamperConfig.md)| The PDF stamper configuration | 

### Return type

[**StamperConfigResponse**](StamperConfigResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_configuration**
> StamperConfigResponse delete_configuration(config_id)

Delete PDF stamper configuration

Delete a PDF stamper configuration.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigApi()
config_id = 'config_id_example' # str | The PDF stamper configuration id

try: 
    # Delete PDF stamper configuration
    api_response = api_instance.delete_configuration(config_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConfigApi->delete_configuration: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**| The PDF stamper configuration id | 

### Return type

[**StamperConfigResponse**](StamperConfigResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_resources**
> delete_resources(config_id, stream_locations)

Delete resources

Delete resources referenced by a configuration.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigApi()
config_id = 'config_id_example' # str | The PDF stamper configuration id
stream_locations = [swagger_client.StreamLocation()] # list[StreamLocation] | The resource locations in storage

try: 
    # Delete resources
    api_instance.delete_resources(config_id, stream_locations)
except ApiException as e:
    print "Exception when calling ConfigApi->delete_resources: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**| The PDF stamper configuration id | 
 **stream_locations** | [**list[StreamLocation]**](StreamLocation.md)| The resource locations in storage | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_configuration**
> StamperConfigResponse get_configuration(config_id)

Get PDF stamper configuration

Retrieve a PDF stamper configuration.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigApi()
config_id = 'config_id_example' # str | The PDF stamper configuration id

try: 
    # Get PDF stamper configuration
    api_response = api_instance.get_configuration(config_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConfigApi->get_configuration: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**| The PDF stamper configuration id | 

### Return type

[**StamperConfigResponse**](StamperConfigResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_configuration**
> StamperConfigResponse update_configuration(config_id, stamp_configuration)

Update PDF stamper configuration

Update an existing PDF stamper configuration.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigApi()
config_id = 'config_id_example' # str | The PDF stamper configuration id
stamp_configuration = swagger_client.StamperConfig() # StamperConfig | The PDF stamper configuration

try: 
    # Update PDF stamper configuration
    api_response = api_instance.update_configuration(config_id, stamp_configuration)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConfigApi->update_configuration: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**| The PDF stamper configuration id | 
 **stamp_configuration** | [**StamperConfig**](StamperConfig.md)| The PDF stamper configuration | 

### Return type

[**StamperConfigResponse**](StamperConfigResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_resource**
> StreamLocation upload_resource(config_id, stream)

Upload a configuration resource

Upload a resource needed by a configuration.

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigApi()
config_id = 'config_id_example' # str | configId
stream = '/path/to/file.txt' # file | The resource data

try: 
    # Upload a configuration resource
    api_response = api_instance.upload_resource(config_id, stream)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ConfigApi->upload_resource: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**| configId | 
 **stream** | **file**| The resource data | 

### Return type

[**StreamLocation**](StreamLocation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

