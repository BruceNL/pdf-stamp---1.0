# DefaultJobSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variables** | **dict(str, str)** | A map with key-values used to replace template variables in components. These are optional defaults. Values in job specific variables will overwrite default values. | [optional] 
**result_settings** | [**ResultSettings**](ResultSettings.md) | The default result file and lifecycle settings | [optional] 
**form_fields** | **dict(str, str)** | Form fields are filled out in PDF forms. These are default values used in the job. Please note that these are different from variables, as the latter can only be used for text, barcode and hyperlink components, whilst the form-fields as the name implies are for filling out PDF forms | [optional] 
**input_settings** | [**InputSettings**](InputSettings.md) | The default input file and lifecycle settings | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


