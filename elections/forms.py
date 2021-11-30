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

    def save(self, *args, **kargs):
        election = super().save(commit=False)
        election.save()
