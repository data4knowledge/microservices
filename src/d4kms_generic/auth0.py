from fastapi import FastAPI, Request, HTTPException, status
from authlib.integrations.starlette_client import OAuth
from starlette.middleware.sessions import SessionMiddleware
from d4kms_generic.service_environment import ServiceEnvironment

# AUTH0_SESSION_SECRET=<secret>
# AUTH0_DOMAIN=<domain>
# AUTH0_CLIENT_ID=<client id>
# AUTH0_CLIENT_SECRET=<client secret>
# AUTH0_AUDIENCE=<audience>

class Auth0():

  def __init__(self, app: FastAPI) -> None:
    se = ServiceEnvironment()
    secret = se.get('AUTH0_SESSION_SECRET')
    app.add_middleware(SessionMiddleware, secret_key=secret)
    self.oauth = None
    self.audience = se.get('AUTH0_AUDIENCE')
    self.domain = se.get('AUTH0_DOMAIN')
    self.client_id = se.get('AUTH0_CLIENT_ID')
    self.client_secret = se.get('AUTH0_CLIENT_SECRET')

  def register(self) -> None:
    """
    Since you have a WebApp you need OAuth client registration so you can perform
    authorization flows with the authorization server
    """
    se = ServiceEnvironment()
    self.oauth = OAuth()
    self.oauth.register(
      "auth0",
      client_id=self.client_id,
      client_secret=self.client_secret,
      client_kwargs={"scope": "openid profile email"},
      server_metadata_url=f'https://{self.domain}/.well-known/openid-configuration'
    )

  def protect_endpoint(request: Request) -> None:
    """
    This Dependency protects an endpoint and it can only be accessed if the user has an active session
    """
    if not 'id_token' in request.session:  
      # it could be userinfo instead of id_token
      # this will redirect people to the login after if they are not logged in
      raise HTTPException(
        status_code=status.HTTP_307_TEMPORARY_REDIRECT, 
        detail="Not authorized",
        headers={"Location": "/login"}
      )
