from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from oauth2client.django_orm import CredentialsField
from oauth2client.django_orm import Storage
import httplib2
from apiclient.discovery import build


class UserProfile(models.Model):
    user = models.ForeignKey(User, primary_key=True)
    credential = CredentialsField()

    def get_credentials(self):
        storage = Storage(UserProfile, "user", self.user, "credential")
        credentials = storage.get()
        return credentials


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = UserProfile(user=instance)
        profile.save()

post_save.connect(create_user_profile, sender=User)


class Calendar(object):
    def __init__(self, user):
        user_profile = user.get_profile()
        credentials = user_profile.get_credentials()
        http = httplib2.Http()
        http = credentials.authorize(http)
        self.service = build("calendar", "v3", http=http)

    def get_events(self):
        events_object = self.service.events()
        response = events_object.list(calendarId="primary").execute()
        return response["items"]

    def add_event(self, summary, start, end):
        # Datetime is converted to RFC3339.
        event = {"summary": summary,
                 "start": {"dateTime": start.isoformat("T") + "Z"},
                 "end": {"dateTime": end.isoformat("T") + "Z"}}
        events_object = self.service.events()
        events_object.insert(calendarId="primary", body=event).execute()

    def delete_event(self, event_id):
        events_object = self.service.events()
        events_object.delete(calendarId="primary", eventId=event_id).execute()
