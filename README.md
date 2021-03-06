# Kleister: SDK for Python

[![Build Status](https://cloud.drone.io/api/badges/gomematic/gomematic-python/status.svg)](https://cloud.drone.io/gomematic/gomematic-python)
[![Join the Matrix chat at https://matrix.to/#/#gomematic:matrix.org](https://img.shields.io/badge/matrix-%23gomematic%3Amatrix.org-7bc9a4.svg)](https://matrix.to/#/#gomematic:matrix.org)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/a9bb2351a4994cad95380830d7296b75)](https://www.codacy.com/app/gomematic/gomematic-python?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=gomematic/gomematic-python&amp;utm_campaign=Badge_Grade)
[![PyPI version](https://badge.fury.io/py/gomematic.svg)](https://badge.fury.io/py/gomematic)

**This project is under heavy development, it's not in a working state yet!**

This repository provides a client SDK for Python. This SDK is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0-alpha1
- Package version: 1.0.0-alpha1
- Build package: org.openapitools.codegen.languages.PythonClientCodegen


## Installation


### Install with `pip`

If you want to install a published version, you just need to execute this command to get the SDK installed via `pip`:

```bash
pip install gomematic
```

After the installation you can simply start to import the SDK:

```python
import gomematic
```


### Install with `setuptools`

If you want to install a unpublished version you can simply clone this repository and use `setuptools` to install the SDK:

```bash
python setup.py install --user
```

After the installation you can simply start to import the SDK:

```python
import gomematic
```


## Getting Started

Please follow the [installation](#installation) instructions and then run the following code:

```python
from __future__ import print_function
from pprint import pprint
import time
import gomematic
from gomematic.rest import ApiException

configuration = gomematic.Configuration()
# Configure HTTP basic authorization: Basic
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = gomematic.Configuration()
# Configure API key authorization: Header
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

api = gomematic.AuthApi(gomematic.ApiClient(configuration))
auth_login = gomematic.AuthLogin() # AuthLogin | The credentials to authenticate

try:
    # Authenticate an user by credentials
    resp = api.login_user(auth_login)
    pprint(resp)
except ApiException as e:
    print("Exception when calling AuthApi->login_user: %s\n" % e)

```


## Documentation for endpoints

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthApi* | [**login_user**](docs/AuthApi.md#login_user) | **POST** /auth/login | Authenticate an user by credentials
*AuthApi* | [**refresh_auth**](docs/AuthApi.md#refresh_auth) | **GET** /auth/refresh | Refresh an auth token before it expires
*AuthApi* | [**verify_auth**](docs/AuthApi.md#verify_auth) | **GET** /auth/verify | Verify validity for an authentication token
*ProfileApi* | [**show_profile**](docs/ProfileApi.md#show_profile) | **GET** /profile/self | Fetch profile details of the personal account
*ProfileApi* | [**token_profile**](docs/ProfileApi.md#token_profile) | **GET** /profile/token | Retrieve an unlimited auth token
*ProfileApi* | [**update_profile**](docs/ProfileApi.md#update_profile) | **PUT** /profile/self | Update your own profile information
*TeamApi* | [**append_team_to_user**](docs/TeamApi.md#append_team_to_user) | **POST** /teams/{team_id}/users | Assign a user to team
*TeamApi* | [**create_team**](docs/TeamApi.md#create_team) | **POST** /teams | Create a new team
*TeamApi* | [**delete_team**](docs/TeamApi.md#delete_team) | **DELETE** /teams/{team_id} | Delete a specific team
*TeamApi* | [**delete_team_from_user**](docs/TeamApi.md#delete_team_from_user) | **DELETE** /teams/{team_id}/users | Remove a user from team
*TeamApi* | [**list_team_users**](docs/TeamApi.md#list_team_users) | **GET** /teams/{team_id}/users | Fetch all users assigned to team
*TeamApi* | [**list_teams**](docs/TeamApi.md#list_teams) | **GET** /teams | Fetch all available teams
*TeamApi* | [**permit_team_user**](docs/TeamApi.md#permit_team_user) | **PUT** /teams/{team_id}/users | Update user perms for team
*TeamApi* | [**show_team**](docs/TeamApi.md#show_team) | **GET** /teams/{team_id} | Fetch a specific team
*TeamApi* | [**update_team**](docs/TeamApi.md#update_team) | **PUT** /teams/{team_id} | Update a specific team
*UserApi* | [**append_user_to_team**](docs/UserApi.md#append_user_to_team) | **POST** /users/{user_id}/teams | Assign a team to user
*UserApi* | [**create_user**](docs/UserApi.md#create_user) | **POST** /users | Create a new user
*UserApi* | [**delete_user**](docs/UserApi.md#delete_user) | **DELETE** /users/{user_id} | Delete a specific user
*UserApi* | [**delete_user_from_team**](docs/UserApi.md#delete_user_from_team) | **DELETE** /users/{user_id}/teams | Remove a team from user
*UserApi* | [**list_user_teams**](docs/UserApi.md#list_user_teams) | **GET** /users/{user_id}/teams | Fetch all teams assigned to user
*UserApi* | [**list_users**](docs/UserApi.md#list_users) | **GET** /users | Fetch all available users
*UserApi* | [**permit_user_team**](docs/UserApi.md#permit_user_team) | **PUT** /users/{user_id}/teams | Update team perms for user
*UserApi* | [**show_user**](docs/UserApi.md#show_user) | **GET** /users/{user_id} | Fetch a specific user
*UserApi* | [**update_user**](docs/UserApi.md#update_user) | **PUT** /users/{user_id} | Update a specific user


## Documentation for models

 - [AuthLogin](docs/AuthLogin.md)
 - [AuthToken](docs/AuthToken.md)
 - [AuthVerify](docs/AuthVerify.md)
 - [GeneralError](docs/GeneralError.md)
 - [Profile](docs/Profile.md)
 - [Team](docs/Team.md)
 - [TeamUser](docs/TeamUser.md)
 - [TeamUserParams](docs/TeamUserParams.md)
 - [User](docs/User.md)
 - [UserTeamParams](docs/UserTeamParams.md)
 - [ValidationError](docs/ValidationError.md)
 - [ValidationErrorErrors](docs/ValidationErrorErrors.md)


## Documentation For authorization


## Basic

- **Type**: HTTP basic authentication


## Header

- **Type**: API key
- **API key parameter name**: X-API-Key
- **Location**: HTTP header



## Security

If you find a security issue please contact gomematic@webhippie.de first.


## Contributing

Fork -> Patch -> Push -> Pull Request


## Authors

* [Thomas Boerger](https://github.com/tboerger)


## License

Apache-2.0


## Copyright

```
Copyright (c) 2018 Thomas Boerger <thomas@webhippie.de>
```

