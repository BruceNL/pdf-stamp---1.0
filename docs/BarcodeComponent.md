# BarcodeComponent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**border** | [**Border**](Border.md) | The border of the component | [optional] 
**connectors** | [**list[Connector]**](Connector.md) | Connectors containing components that can be positioned relative to this component | [optional] 
**offset** | [**Point**](Point.md) | The offset of the component relative to the parent component | [optional] 
**error_correction_level** | **str** | Specifies what degree of error correction to use, for example in QR Codes, See ISO 18004:2006, 6.5.1. This enum encapsulates the four error correction levels defined by the QR code standard | [optional] 
**barcode_format** | **str** | The barcode format to generate | 
**width** | **int** | The preferred width in pixels | 
**content** | **str** | The contents to encode in the barcode | 
**height** | **int** | The preferred height in pixels | 
**qr_version** | **int** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


