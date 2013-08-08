from django.test import TestCase
from django.http import HttpResponseRedirect
from test_utils import TestCaseWithAuthentication


class LoginTests(TestCase):
    def test_redirect_login_url(self):
        """ /login/ endpoint is used for redirection to Google OAuth."""
        r = self.client.get("/login/")
        self.assertEqual(r.status_code, HttpResponseRedirect.status_code)
        self.assertIn("https://accounts.google.com/o/oauth2/auth",
                      r["Location"])

    def test_oauth2callback_without_login_attempt(self):
        """ /oauth2callback/ endpoint when called without valid
        OAuth data returns 401."""
        r = self.client.get("/oauth2callback/")
        self.assertEqual(r.status_code, 401)


class EventTests(TestCaseWithAuthentication):
    def test_add_event_with_wrong_start_and_end_datetime(self):
        """End time cannot be earlier than start time."""
        r = self.client.post("/add_event/", {"summary": "Some summary",
                                             "start": "06/23/2013 12:30",
                                             "end": "06/23/2013 12:29"})
        self.assertIn("End time cannot be earlier than start time.",
                      r.content)
