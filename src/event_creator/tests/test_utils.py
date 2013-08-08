from django.test import TestCase
import event_creator.auth


class TestCaseWithAuthentication(TestCase):
    def setUp(self):
        id_token = {"sub": "username", "email": "username@username.username"}
        self.client.login(id_token=id_token)

    def tearDown(self):
        self.client.logout()


def check_credentials_mock(function):
    def wrap(request, *args, **kwargs):
        return function(request, *args, **kwargs)
    return wrap

event_creator.auth.check_credentials = check_credentials_mock
