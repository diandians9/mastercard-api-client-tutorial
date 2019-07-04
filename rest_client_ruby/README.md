# swagger_client

SwaggerClient - the Ruby gem for the MDES for Merchants

The MDES APIs are designed as RPC style stateless web services where each API endpoint represents an operation to be performed.  All request and response payloads are sent in the JSON (JavaScript Object Notation) data-interchange format. Each endpoint in the API specifies the HTTP Method used to access it. All strings in request and response objects are to be UTF-8 encoded.  Each API URI includes the major and minor version of API that it conforms to.  This will allow multiple concurrent versions of the API to be deployed simultaneously.  

This SDK is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.2.7
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.RubyClientCodegen

## Installation

### Build a gem

To build the Ruby code into a gem:

```shell
gem build swagger_client.gemspec
```

Then either install the gem locally:

```shell
gem install ./swagger_client-1.0.0.gem
```
(for development, run `gem install --dev ./swagger_client-1.0.0.gem` to install the development dependencies)

or publish the gem to a gem hosting service, e.g. [RubyGems](https://rubygems.org/).

Finally add this to the Gemfile:

    gem 'swagger_client', '~> 1.0.0'

### Install from Git

If the Ruby gem is hosted at a git repository: https://github.com/GIT_USER_ID/GIT_REPO_ID, then add the following in the Gemfile:

    gem 'swagger_client', :git => 'https://github.com/GIT_USER_ID/GIT_REPO_ID.git'

### Include the Ruby code directly

Include the Ruby code directly using `-I` as follows:

```shell
ruby -Ilib script.rb
```

## Getting Started

Please follow the [installation](#installation) procedure and then run the following code:
```ruby
# Load the gem
require 'swagger_client'

api_instance = SwaggerClient::DeleteApi.new

opts = { 
  delete_request_schema: SwaggerClient::DeleteRequestSchema.new # DeleteRequestSchema | Contains the details of the request message. 
}

begin
  #Used to delete one or more Tokens. The API is limited to 10 Tokens per request.
  result = api_instance.delete_digitization(opts)
  p result
rescue SwaggerClient::ApiError => e
  puts "Exception when calling DeleteApi->delete_digitization: #{e}"
end

```

## Documentation for API Endpoints

All URIs are relative to *https://api.mastercard.com/mdes*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*SwaggerClient::DeleteApi* | [**delete_digitization**](docs/DeleteApi.md#delete_digitization) | **POST** /digitization/static/1/0/delete | Used to delete one or more Tokens. The API is limited to 10 Tokens per request.
*SwaggerClient::GetAssetApi* | [**get_asset**](docs/GetAssetApi.md#get_asset) | **GET** /assets/static/1/0/asset/{AssetId} | Used to retrieve static Assets from MDES�s repository, such as Card art, MasterCard brand logos, Issuer logos, and Terms and Conditions.
*SwaggerClient::GetTaskStatusApi* | [**get_task_status**](docs/GetTaskStatusApi.md#get_task_status) | **POST** /digitization/static/1/0/getTaskStatus | Used to check the status of any asynchronous task that was previously requested.
*SwaggerClient::GetTokenApi* | [**get_token**](docs/GetTokenApi.md#get_token) | **POST** /digitization/static/1/0/getToken | Used to get the status and details of a single given Token.
*SwaggerClient::NotifyTokenUpdatedApi* | [**notify_token_update__for_token_state_change**](docs/NotifyTokenUpdatedApi.md#notify_token_update__for_token_state_change) | **POST** /digitization/static/1/0/notifyTokenUpdated | Outbound API used by MDES to notify the Token Requestor of significant Token updates, such as when the Token is activated, suspended, unsuspended or deleted; or when information about the Token or its product configuration has changed.
*SwaggerClient::SearchTokensApi* | [**search_tokens**](docs/SearchTokensApi.md#search_tokens) | **POST** /digitization/static/1/0/searchTokens | Used to get basic token information for all tokens on a specified device, or all tokens mapped to the given Account PAN.
*SwaggerClient::SuspendApi* | [**create_suspend**](docs/SuspendApi.md#create_suspend) | **POST** /digitization/static/1/0/suspend | Used to temporarily suspend one or more Tokens (for example, suspending all Tokens on a device in response to the device being lost).  The API is limited to 10 Tokens per request.
*SwaggerClient::TokenizeApi* | [**create_tokenize**](docs/TokenizeApi.md#create_tokenize) | **POST** /digitization/static/1/0/tokenize | Used to digitize a card to create a server-based Token.
*SwaggerClient::TransactApi* | [**create_transact**](docs/TransactApi.md#create_transact) | **POST** /remotetransaction/static/1/0/transact | Used by the Token Requestor to create a Digital Secure Remote Payment (\"DSRP\") transaction cryptogram using the credentials stored within MDES in order to perform a DSRP transaction.
*SwaggerClient::UnsuspendApi* | [**create_unsuspend**](docs/UnsuspendApi.md#create_unsuspend) | **POST** /digitization/static/1/0/unsuspend | Used to unsuspend one or more previously suspended Tokens. The API is limited to 10 Tokens per request.


## Documentation for Models

 - [SwaggerClient::AssetResponseSchema](docs/AssetResponseSchema.md)
 - [SwaggerClient::AuthenticationMethods](docs/AuthenticationMethods.md)
 - [SwaggerClient::BillingAddress](docs/BillingAddress.md)
 - [SwaggerClient::CardInfo](docs/CardInfo.md)
 - [SwaggerClient::CardInfoData](docs/CardInfoData.md)
 - [SwaggerClient::DecisioningData](docs/DecisioningData.md)
 - [SwaggerClient::DeleteRequestSchema](docs/DeleteRequestSchema.md)
 - [SwaggerClient::DeleteResponseSchema](docs/DeleteResponseSchema.md)
 - [SwaggerClient::EncryptedPayload](docs/EncryptedPayload.md)
 - [SwaggerClient::EncryptedPayloadTransact](docs/EncryptedPayloadTransact.md)
 - [SwaggerClient::Error](docs/Error.md)
 - [SwaggerClient::ErrorsResponse](docs/ErrorsResponse.md)
 - [SwaggerClient::GetTaskStatusRequestSchema](docs/GetTaskStatusRequestSchema.md)
 - [SwaggerClient::GetTaskStatusResponseSchema](docs/GetTaskStatusResponseSchema.md)
 - [SwaggerClient::GetTokenRequestSchema](docs/GetTokenRequestSchema.md)
 - [SwaggerClient::GetTokenResponseSchema](docs/GetTokenResponseSchema.md)
 - [SwaggerClient::MediaContent](docs/MediaContent.md)
 - [SwaggerClient::NotifyTokenEncryptedPayload](docs/NotifyTokenEncryptedPayload.md)
 - [SwaggerClient::NotifyTokenUpdatedRequestSchema](docs/NotifyTokenUpdatedRequestSchema.md)
 - [SwaggerClient::NotifyTokenUpdatedResponseSchema](docs/NotifyTokenUpdatedResponseSchema.md)
 - [SwaggerClient::ProductConfig](docs/ProductConfig.md)
 - [SwaggerClient::SearchTokensRequestSchema](docs/SearchTokensRequestSchema.md)
 - [SwaggerClient::SearchTokensResponseSchema](docs/SearchTokensResponseSchema.md)
 - [SwaggerClient::SuspendRequestSchema](docs/SuspendRequestSchema.md)
 - [SwaggerClient::SuspendResponseSchema](docs/SuspendResponseSchema.md)
 - [SwaggerClient::Token](docs/Token.md)
 - [SwaggerClient::TokenDetail](docs/TokenDetail.md)
 - [SwaggerClient::TokenDetailData](docs/TokenDetailData.md)
 - [SwaggerClient::TokenDetailDataPAR](docs/TokenDetailDataPAR.md)
 - [SwaggerClient::TokenDetailTokenizeResponse](docs/TokenDetailTokenizeResponse.md)
 - [SwaggerClient::TokenForLCM](docs/TokenForLCM.md)
 - [SwaggerClient::TokenInfo](docs/TokenInfo.md)
 - [SwaggerClient::TokenizeRequestSchema](docs/TokenizeRequestSchema.md)
 - [SwaggerClient::TokenizeResponseSchema](docs/TokenizeResponseSchema.md)
 - [SwaggerClient::TransactEncryptedData](docs/TransactEncryptedData.md)
 - [SwaggerClient::TransactError](docs/TransactError.md)
 - [SwaggerClient::TransactRequestSchema](docs/TransactRequestSchema.md)
 - [SwaggerClient::TransactResponseSchema](docs/TransactResponseSchema.md)
 - [SwaggerClient::UnSuspendRequestSchema](docs/UnSuspendRequestSchema.md)
 - [SwaggerClient::UnSuspendResponseSchema](docs/UnSuspendResponseSchema.md)


## Documentation for Authorization

 All endpoints do not require authorization.
