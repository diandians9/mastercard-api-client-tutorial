# GetAssetApi

All URIs are relative to *https://api.mastercard.com/mdes*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAsset**](GetAssetApi.md#getAsset) | **GET** /assets/static/1/0/asset/{AssetId} | Used to retrieve static Assets from MDES�s repository, such as Card art, MasterCard brand logos, Issuer logos, and Terms and Conditions.


<a name="getAsset"></a>
# **getAsset**
> AssetResponseSchema getAsset(assetId)

Used to retrieve static Assets from MDES�s repository, such as Card art, MasterCard brand logos, Issuer logos, and Terms and Conditions.

This API is used to retrieve static Assets from MDES�s repository, such as - Card art, MasterCard brand logos, Issuers� logos, and Terms and Conditions. Every Asset in the repository is referenced using an Asset ID. Once an Asset has been assigned to an Asset ID, the contents of the Asset will not change. If contents do need to change (for example, Issuer has supplied new artwork for a product), they will be updated in the repository and be assigned a new Asset ID.  Different types of Assets are supported in the repository, such as images and text files; and for each type of Asset, multiple formats may be supported. For example, a single image Asset may be supported in various file formats; or variant sizes, allowing the Token Requestor to select the most appropriate format to use for a particular target device. 

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.GetAssetApi;


GetAssetApi apiInstance = new GetAssetApi();
String assetId = "assetId_example"; // String | An Asset ID corresponds to an individual Digital Asset. Digital Assets are returned as part of the Product Configuration from the Tokenize Response. The Asset ID itself is supplied as a Get request in the form of https://{INSERT ENVIRONMENT URL HERE}/mdes/assets/static/1/0/asset/{AssetID} - See JSON examples for details.  
try {
    AssetResponseSchema result = apiInstance.getAsset(assetId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling GetAssetApi#getAsset");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assetId** | **String**| An Asset ID corresponds to an individual Digital Asset. Digital Assets are returned as part of the Product Configuration from the Tokenize Response. The Asset ID itself is supplied as a Get request in the form of https://{INSERT ENVIRONMENT URL HERE}/mdes/assets/static/1/0/asset/{AssetID} - See JSON examples for details.   |

### Return type

[**AssetResponseSchema**](AssetResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json
