from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from oauth2client.django_orm import Storage
from oauth2client.client import FlowExchangeError
import apiclient.errors
from auth import flow, check_credentials
from models import UserProfile, Calendar
from forms import AddEventForm


@check_credentials
def index(request):
    events = None
    if request.user.is_authenticated():
        calendar = Calendar(request.user)
        events = calendar.get_events()
    return render(request, "index.html", {"events": events})


@login_required
@check_credentials
@require_http_methods(["GET", "POST"])
def add_event(request):
    if request.method == "GET":
        add_event_form = AddEventForm()
    elif request.method == "POST":
        add_event_form = AddEventForm(request.POST)
        if add_event_form.is_valid():
            calendar = Calendar(request.user)
            try:
                calendar.add_event(add_event_form.cleaned_data["summary"],
                                   add_event_form.cleaned_data["start"],
                                   add_event_form.cleaned_data["end"])
            except apiclient.errors.HttpError:
                return HttpResponse("Calendar event was not added", status=500)
            return redirect(reverse("event_creator.views.index"))
    return render(request,
                  "add_event.html",
                  {"add_event_form": add_event_form,
                   "action": request.get_full_path()})


@login_required
@check_credentials
def delete_event(request, event_id):
    calendar = Calendar(request.user)
    try:
        calendar.delete_event(event_id)
        return redirect(reverse("event_creator.views.index"))
    except apiclient.errors.HttpError:
        return HttpResponse("Calendar event was not deleted", status=500)


def oauth2redirect(request):
    auth_uri = flow.step1_get_authorize_url()
    return redirect(auth_uri)


def oauth2callback(request):
    try:
        credentials = flow.step2_exchange(request.REQUEST)
    except FlowExchangeError:
        return HttpResponse("Access denied", status=401)
    user = authenticate(id_token=credentials.id_token)
    login(request, user)
    storage = Storage(UserProfile, "user", user, "credential")
    storage.put(credentials)
    return redirect(reverse("event_creator.views.index"))
