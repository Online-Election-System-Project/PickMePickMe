from django.shortcuts import render
from django.views.generic import FormView, ListView
from django.urls import reverse_lazy

from . import forms

# Create your views here.


class ElectionRegisterView(FormView):
    template_name = "elections/register.html"
    form_class = forms.ElectionRegisterForm
    success_url = reverse_lazy("elections:election-register")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
