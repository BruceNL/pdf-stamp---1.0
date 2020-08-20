# PdfStamperJobRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_lifecycles** | [**list[Lifecycle]**](Lifecycle.md) | The lifecycles of the job itself | [optional] 
**inline_config** | [**StamperConfig**](StamperConfig.md) | Optional job specific config that can be supplied inline. Will be merged with the specified configuration.  | [optional] 
**variables** | **dict(str, str)** | A map with key-values used to replace template variables in components. | [optional] 
**result_settings** | [**ResultSettings**](ResultSettings.md) | The result file and lifecycle settings | [optional] 
**config_ids** | **list[str]** | A list of configuration ids that have to be applied during executing the job. | 
**input_results** | [**list[InputResultLocation]**](InputResultLocation.md) | The input(s) and optional result(s) | 
**form_fields** | **dict(str, str)** | A map with key-values used to input values in a PDF form. | [optional] 
**input_settings** | [**InputSettings**](InputSettings.md) | The input file and lifecycle settings | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


