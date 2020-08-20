# StamperConfigResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_resources** | [**list[StreamLocation]**](StreamLocation.md) | Any registered resource used by the configuration | [optional] 
**creation_time** | **datetime** | The creation date/time of the initial configuration in ISO 8601 format | [optional] 
**config_id** | **str** | The configuration id | [optional] 
**name** | **str** | An optional configuration name | [optional] 
**update_time** | **datetime** | The last update date/time of this configuration in ISO 8601 format | [optional] 
**config_status** | **str** | The status of the config action | [optional] 
**config** | [**StamperConfig**](StamperConfig.md) | The PDF stamper configuration | [optional] 
**status_message** | **str** | A status message, which can be informational, warning or error. A message here does not indicate an error per se | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


