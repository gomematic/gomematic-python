# gomematic.ProfileApi

All URIs are relative to *http://try.gomematic.tech/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**show_profile**](ProfileApi.md#show_profile) | **GET** /profile/self | Fetch profile details of the personal account
[**token_profile**](ProfileApi.md#token_profile) | **GET** /profile/token | Retrieve an unlimited auth token
[**update_profile**](ProfileApi.md#update_profile) | **PUT** /profile/self | Update your own profile information


# **show_profile**
> Profile show_profile()

Fetch profile details of the personal account

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
api_instance = gomematic.ProfileApi(gomematic.ApiClient(configuration))

try:
    # Fetch profile details of the personal account
    api_response = api_instance.show_profile()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfileApi->show_profile: %s\n" % e)
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
api_instance = gomematic.ProfileApi(gomematic.ApiClient(configuration))

try:
    # Fetch profile details of the personal account
    api_response = api_instance.show_profile()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfileApi->show_profile: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Profile**](Profile.md)

### Authorization

[Basic](../README.md#Basic), [Header](../README.md#Header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **token_profile**
> AuthToken token_profile()

Retrieve an unlimited auth token

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
api_instance = gomematic.ProfileApi(gomematic.ApiClient(configuration))

try:
    # Retrieve an unlimited auth token
    api_response = api_instance.token_profile()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfileApi->token_profile: %s\n" % e)
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
api_instance = gomematic.ProfileApi(gomematic.ApiClient(configuration))

try:
    # Retrieve an unlimited auth token
    api_response = api_instance.token_profile()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfileApi->token_profile: %s\n" % e)
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

# **update_profile**
> Profile update_profile(profile)

Update your own profile information

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
api_instance = gomematic.ProfileApi(gomematic.ApiClient(configuration))
profile = gomematic.Profile() # Profile | The profile data to update

try:
    # Update your own profile information
    api_response = api_instance.update_profile(profile)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfileApi->update_profile: %s\n" % e)
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
api_instance = gomematic.ProfileApi(gomematic.ApiClient(configuration))
profile = gomematic.Profile() # Profile | The profile data to update

try:
    # Update your own profile information
    api_response = api_instance.update_profile(profile)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfileApi->update_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile** | [**Profile**](Profile.md)| The profile data to update | 

### Return type

[**Profile**](Profile.md)

### Authorization

[Basic](../README.md#Basic), [Header](../README.md#Header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

