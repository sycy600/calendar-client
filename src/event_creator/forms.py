from django import forms
from django.core.exceptions import ValidationError


class AddEventForm(forms.Form):
    summary = forms.CharField()
    start = forms.DateTimeField()
    end = forms.DateTimeField()

    def clean(self):
        cleaned_data = super(AddEventForm, self).clean()
        if "start" not in cleaned_data or "end" not in cleaned_data:
            return cleaned_data
        if cleaned_data["start"] > cleaned_data["end"]:
            raise ValidationError(u"End time cannot be earlier "
                                  "than start time.")
        return cleaned_data
