from auth0.management import Auth0
from d4kms_generic.auth0_management import Auth0Management
from tests.mocks.mock_general import *

def test_init(mocker):
  gti = mock_get_token_instance(mocker)
  cc = mock_client_credentials(mocker)
  ami = mock_auth0_management_instance(mocker)
  a0m = Auth0Management()
  assert mock_called(gti)
  assert mock_called(cc)
  assert mock_called(ami)
  mock_parameters_correct(gti, [mocker.call('dev-something.eu.auth0.com', 'client-id', 'client-secret')])
  mock_parameters_correct(cc, [mocker.call('https://dev-something.eu.auth0.com/api/v2/')])
  mock_parameters_correct(ami, [mocker.call('dev-something.eu.auth0.com', '1234-5678-token')])

def test_user_list(mocker, PropertyMock):
  gti = mock_get_token_instance(mocker)
  cc = mock_client_credentials(mocker)
  ma = mock_attribute(mocker, PropertyMock)
  a0m = Auth0Management()
  result = a0m.user_list()
  assert mock_called(ul)
  mock_parameters_correct(ul, [mocker.call()])

def test_user_roles(mocker, PropertyMock):
  gti = mock_get_token_instance(mocker)
  cc = mock_client_credentials(mocker)
  ma = mock_attribute(mocker, PropertyMock)
  a0m = Auth0Management()
  result = a0m.user_roles('user-id')
  assert mock_called(ul)
  mock_parameters_correct(ul, [mocker.call('user-id')])

def mock_auth0_management_instance(mocker):
  item = mocker.patch("auth0.management.Auth0.__init__")
  item.side_effect = [None]
  return item

# def mock_user_list(mocker):
#   item = mocker.patch("auth0.management.Users.list")
#   item.side_effect = [None]
#   return item

# def mock_user_roles(mocker):
#   item = mocker.patch("auth0.management.Users.list_roles")
#   item.side_effect = [['roles']]
#   return item

def mock_get_token_instance(mocker):
  item = mocker.patch("auth0.authentication.GetToken.__init__")
  item.side_effect = [None]
  return item

def mock_client_credentials(mocker):
  item = mocker.patch("auth0.authentication.GetToken.client_credentials")
  item.side_effect = [{'access_token': '1234-5678-token'}]
  return item

class FakeUser():
  def list():
    return ['list']
  def list_roles():
    return ['roles']

def mock_attribute(mocker, PropertyMock):
  ma = mocker.patch.object(Auth0, "users", new_callable=PropertyMock)
  ma.return_value = FakeUser()


