from auth0.management import Auth0
from d4kms_generic.auth0_management import Auth0Management
from tests.mocks.mock_general import *
from unittest.mock import PropertyMock

def test_init():
  a0m = Auth0Management()
  assert a0m._domain == "dev-something.eu.auth0.com"
  assert a0m._client_id == "client-id"
  assert a0m._client_secret == "client-secret"
  assert a0m._auth0 == None

def test_token(mocker):
  gti = mock_get_token_instance(mocker)
  cc = mock_client_credentials(mocker)
  ami = mock_auth0_management_instance(mocker)
  a0m = Auth0Management()
  a0m.token()
  assert mock_called(gti)
  assert mock_called(cc)
  assert mock_called(ami)
  mock_parameters_correct(gti, [mocker.call('dev-something.eu.auth0.com', 'client-id', 'client-secret')])
  mock_parameters_correct(cc, [mocker.call('https://dev-something.eu.auth0.com/api/v2/')])
  mock_parameters_correct(ami, [mocker.call('dev-something.eu.auth0.com', '1234-5678-token', rest_options=None)])

def mock_auth0_management_instance(mocker):
  item = mocker.patch("auth0.management.auth0.Auth0.__init__")
  item.side_effect = [None]
  return item

def mock_get_token_instance(mocker):
  item = mocker.patch("auth0.authentication.GetToken.__init__")
  item.side_effect = [None]
  return item

def mock_client_credentials(mocker):
  item = mocker.patch("auth0.authentication.GetToken.client_credentials")
  item.side_effect = [{'access_token': '1234-5678-token'}]
  return item
