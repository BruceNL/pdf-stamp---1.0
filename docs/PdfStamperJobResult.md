# PdfStamperJobResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completion_time** | **datetime** | The completion date/time of this job in ISO 8601 format | [optional] 
**job_id** | **str** | The job id | [optional] 
**request** | [**PdfStamperJobRequest**](PdfStamperJobRequest.md) | The request settings used during executing the PDF Stamper job | [optional] 
**job_status** | **str** | The status of the job | [optional] 
**creation_time** | **datetime** | The creation date/time of this job in ISO 8601 format | [optional] 
**input_results** | [**list[InputResultLocation]**](InputResultLocation.md) | The input(s) and result(s) streamlocation pairs | [optional] 
**update_time** | **datetime** | The last update date/time of this job in ISO 8601 format | [optional] 
**status_message** | **str** | A status message, which can be informational, warning or error. AA message here does not indicate an error per se | [optional] 
**queue_time** | **datetime** | The PDF Stamper queue date/time of this job in ISO 8601 format | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


