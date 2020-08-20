# CanvasComponent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**border** | [**Border**](Border.md) | The border of the component | [optional] 
**specific_pages** | **list[int]** |  | [optional] 
**connectors** | [**list[Connector]**](Connector.md) | Connectors containing components that can be positioned relative to this component | [optional] 
**page_selector** | **str** | Prescribes the page(s) the component needs to be overlay-ed on. | 
**offset** | [**Point**](Point.md) | The offset of the component relative to the parent component | [optional] 
**page_operation** | **str** | The operation that should be executed with the stamp component | 
**position** | **str** | The position where the stamp end up relative to existing content. Only foreground is supported for now | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


