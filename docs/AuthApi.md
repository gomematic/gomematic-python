# gomematic.AuthApi

All URIs are relative to *http://try.gomematic.tech/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login_user**](AuthApi.md#login_user) | **POST** /auth/login | Authenticate an user by credentials
[**refresh_auth**](AuthApi.md#refresh_auth) | **GET** /auth/refresh | Refresh an auth token before it expires
[**verify_auth**](AuthApi.md#verify_auth) | **GET** /auth/verify | Verify validity for an authentication token


# **login_user**
> AuthToken login_user(auth_login)

Authenticate an user by credentials

### Example

* Basic Authentication (Basic):
```python
from __future__ import print_function
import time
import gomematic
from gomematic.rest import ApiException
from pprint import pprint
configuration = gomematic.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = gomematic.Configuration()
# Configure API key authorization: Header
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = gomematic.AuthApi(gomematic.ApiClient(configuration))
auth_login = gomematic.AuthLogin() # AuthLogin | The credentials to authenticate

try:
    # Authenticate an user by credentials
    api_response = api_instance.login_user(auth_login)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->login_user: %s\n" % e)
```

* Api Key Authentication (Header):
```python
from __future__ import print_function
import time
import gomematic
from gomematic.rest import ApiException
from pprint import pprint
configuration = gomematic.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = gomematic.Configuration()
# Configure API key authorization: Header
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = gomematic.AuthApi(gomematic.ApiClient(configuration))
auth_login = gomematic.AuthLogin() # AuthLogin | The credentials to authenticate

try:
    # Authenticate an user by credentials
    api_response = api_instance.login_user(auth_login)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->login_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_login** | [**AuthLogin**](AuthLogin.md)| The credentials to authenticate | 

### Return type

[**AuthToken**](AuthToken.md)

### Authorization

[Basic](../README.md#Basic), [Header](../README.md#Header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_auth**
> AuthToken refresh_auth()

Refresh an auth token before it expires

### Example

* Basic Authentication (Basic):
```python
from __future__ import print_function
import time
import gomematic
from gomematic.rest import ApiException
from pprint import pprint
configuration = gomematic.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = gomematic.Configuration()
# Configure API key authorization: Header
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = gomematic.AuthApi(gomematic.ApiClient(configuration))

try:
    # Refresh an auth token before it expires
    api_response = api_instance.refresh_auth()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->refresh_auth: %s\n" % e)
```

* Api Key Authentication (Header):
```python
from __future__ import print_function
import time
import gomematic
from gomematic.rest import ApiException
from pprint import pprint
configuration = gomematic.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = gomematic.Configuration()
# Configure API key authorization: Header
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = gomematic.AuthApi(gomematic.ApiClient(configuration))

try:
    # Refresh an auth token before it expires
    api_response = api_instance.refresh_auth()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->refresh_auth: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuthToken**](AuthToken.md)

### Authorization

[Basic](../README.md#Basic), [Header](../README.md#Header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_auth**
> AuthVerify verify_auth()

Verify validity for an authentication token

### Example

* Basic Authentication (Basic):
```python
from __future__ import print_function
import time
import gomematic
from gomematic.rest import ApiException
from pprint import pprint
configuration = gomematic.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = gomematic.Configuration()
# Configure API key authorization: Header
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = gomematic.AuthApi(gomematic.ApiClient(configuration))

try:
    # Verify validity for an authentication token
    api_response = api_instance.verify_auth()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->verify_auth: %s\n" % e)
```

* Api Key Authentication (Header):
```python
from __future__ import print_function
import time
import gomematic
from gomematic.rest import ApiException
from pprint import pprint
configuration = gomematic.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = gomematic.Configuration()
# Configure API key authorization: Header
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = gomematic.AuthApi(gomematic.ApiClient(configuration))

try:
    # Verify validity for an authentication token
    api_response = api_instance.verify_auth()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->verify_auth: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuthVerify**](AuthVerify.md)

### Authorization

[Basic](../README.md#Basic), [Header](../README.md#Header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

