from django import forms
from django.forms import fields
from . import models
import elections


class ElectionRegisterForm(forms.ModelForm):
    class Meta:
        model = models.Election
        fields = [
            "title",
            "register_period_begin",
            "register_period_end",
            "election_period_begin",
            "election_period_end",
            "election_type",
        ]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "대한민국 제20대 대통령 선거"}),
            "register_period_begin": forms.DateTimeInput(
                attrs={"placeholder": "2020-01-01 09:00:00"}
            ),
            "register_period_end": forms.DateTimeInput(
                attrs={"placeholder": "2020-01-02 09:00:00"}
            ),
            "election_period_begin": forms.DateTimeInput(
                attrs={"placeholder": "2020-01-11 09:00:00"}
            ),
            "election_period_end": forms.DateTimeInput(
                attrs={"placeholder": "2020-01-12 09:00:00"}
            ),
        }

    def save(self, *args, **kargs):
        election = super().save(commit=False)
        election.save()
