# Lifecycle

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicable_job_statuses** | **list[str]** | Job status needs to be in this list in order for the action to be performed! | [optional] 
**action_time** | **datetime** | The time at which the job and files will be deleted, regardless of whether it has been retrieved or not. Maximal time is 1 day from job creation | [optional] 
**action** | **str** | The action to perform. Currently only delete is supported | [optional] 
**type** | **str** | Determine when to delete the job and associated files.  RETRIEVAL means delete directly after retrieving the PDF file. When the file has not been retrieved before the action time, it will be deleted regardless.  Time means, delete on specific time, regardless of whether it has been processed | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


