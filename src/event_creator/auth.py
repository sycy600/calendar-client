from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from oauth2client.client import OAuth2WebServerFlow

OAUTH_REDIRECT_URI = settings.OAUTH_REDIRECT_BASE + "/oauth2callback"
OAUTH_SCOPES = ('https://www.googleapis.com/auth/calendar '
                'https://www.googleapis.com/auth/userinfo.email')


class OAuth2AuthenticationBackend(object):
    def authenticate(self, id_token):
        try:
            # 'sub' is identifier for user in Google accounts.
            user = User.objects.get(username=id_token["sub"])
        except User.DoesNotExist:
            user = User.objects.create_user(username=id_token["sub"],
                                            email=id_token["email"])
        return user

    def get_user(self, user_id):
        return User.objects.get(id=user_id)


flow = OAuth2WebServerFlow(client_id=settings.OAUTH_CLIENT_ID,
                           client_secret=settings.OAUTH_CLIENT_SECRET,
                           scope=OAUTH_SCOPES,
                           redirect_uri=OAUTH_REDIRECT_URI)


def check_credentials(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated():
            user_profile = request.user.get_profile()
            credentials = user_profile.get_credentials()
            if credentials is None or credentials.invalid:
                return redirect(reverse("event_creator.views.oauth2redirect"))
        return function(request, *args, **kwargs)
    return wrap
