# ContentRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variables** | **dict(str, str)** | A map with key-values used to replace template variables in components. | [optional] 
**filename** | **str** | The filename | 
**config_ids** | **list[str]** | A list of configuration ids that have to be applied during executing the job. | 
**form_fields** | **dict(str, str)** | A map with key-values used to fill out PDF forms. Please not that this is different from using variables. Variables are used in texts, hyperlinks and barcodes | [optional] 
**content** | **str** | The file as a base64 encoded string | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


