from fastapi import FastAPI, Request, HTTPException, status
from authlib.integrations.starlette_client import OAuth
from starlette.middleware.sessions import SessionMiddleware
from d4kms_generic.service_environment import ServiceEnvironment
from d4kms_generic.logger import application_logger
from urllib.parse import quote_plus, urlencode

class Auth0Service():

  def __init__(self, app: FastAPI) -> None:
    se = ServiceEnvironment()
    secret = se.get('AUTH0_SESSION_SECRET')
    app.add_middleware(SessionMiddleware, secret_key=secret)
    self.app = app
    self.oauth = None
    self.audience = se.get('AUTH0_AUDIENCE')
    self.domain = se.get('AUTH0_DOMAIN')
    self.client_id = se.get('AUTH0_CLIENT_ID')
    self.client_secret = se.get('AUTH0_CLIENT_SECRET')
    self.root_url = se.get('ROOT_URL')

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

  async def save_token(self, request: Request):
    token = await self.oauth.auth0.authorize_access_token(request)
    # Store `access_token`, `id_token`, and `userinfo` in session
    request.session['access_token'] = token['access_token']
    request.session['id_token'] = token['id_token']
    request.session['userinfo'] = token['userinfo']
    application_logger.info(f"User {token['userinfo']}")
    
  async def login(self, request: Request, route_method: str) -> None:
    url = self._get_abs_path(route_method)
    application_logger.info(f"Login attempt '{url}")
    return await self.oauth.auth0.authorize_redirect(
      request,
      redirect_uri=url,
      audience=self.audience
    )

  def logout(self, request: Request, route_method: str) -> str:
    request.session.clear()
    url = self._get_abs_path(route_method)
    application_logger.info(f"Logout attempt '{url}")
    data = {"returnTo": url, "client_id": self.client_id}
    url = f"https://{self.domain}/v2/logout?{urlencode(data,quote_via=quote_plus,)}"
    application_logger.info(f"Logout URL '{url}'")
    return url

  def protect_route(self, request: Request, location: str='/login') -> None:
    """
    This Dependency protects an endpoint and it can only be accessed if the user has an active session
    """
    if not 'id_token' in request.session:  
      # it could be userinfo instead of id_token
      # this will redirect people to the login after if they are not logged in
      raise HTTPException(
        status_code=status.HTTP_307_TEMPORARY_REDIRECT, 
        detail="Not authorized",
        headers={"Location": location}
      )

  def _get_abs_path(self, route: str):
    app_domain = self.root_url[:-1] if self.root_url.endswith("/") else self.root_url
    application_logger.info(f"Forming absolute path using '{app_domain}")
    return f"{app_domain}{self.app.url_path_for(route)}"
