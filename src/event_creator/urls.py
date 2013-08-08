from django.conf.urls import patterns, include
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    (r"^$", "event_creator.views.index"),
    (r"^login/$", "event_creator.views.oauth2redirect"),
    (r"^oauth2callback/$", "event_creator.views.oauth2callback"),
    (r"^logout/$", "django.contrib.auth.views.logout", {"next_page": "/"}),
    (r"^add_event/$", "event_creator.views.add_event"),
    (r"^delete_event/(?P<event_id>[a-z0-9]+)/$",
     "event_creator.views.delete_event"),
    (r"^admin/", include(admin.site.urls)),
)
