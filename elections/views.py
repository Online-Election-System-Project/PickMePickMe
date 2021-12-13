from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import ListView, FormView, UpdateView
from django.urls import reverse_lazy, reverse
from django.views.generic.detail import DetailView
from promotion.models import Promotion
import promotion

from . import forms, models


class ElectionListView(ListView):

    """ElectionListView Definition"""

    model = models.Election
    paginate_by = 12
    paginate_orphans = 5
    context_object_name = "elections"


class ElectionDetailView(DetailView):

    """ElectionDetailView Definition"""

    model = models.Election
    template_name = "elections/election_detail.html"


class ElectionRegisterView(FormView):
    template_name = "elections/register.html"
    form_class = forms.ElectionRegisterForm
    success_url = reverse_lazy("elections:election-register")  # todo: 선거 리스트로 보내기

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class EditElectionView(UpdateView):

    model = models.Election
    template_name = "elections/edit-election.html"
    fields = (
        "title",
        "register_period_begin",
        "register_period_end",
        "election_period_begin",
        "election_period_end",
        "election_type",
    )
    success_url = reverse_lazy("elections:election-register")

    def get_object(self, queryset=None):
        # 지금 로그인 한 유저가 superuser가 아니면 404오류 띄우기
        election = super().get_object(queryset=queryset)
        if self.request.user.is_superuser == False:
            raise Http404()
        return election


def acceptRequest(request, pk):
    if request.method == "POST":
        promotion = Promotion.objects.get(pk=pk)
        promotion.status = Promotion.STATUS_ACCEPTED
        promotion.save()
    return redirect("promotion_detail", pk=pk)


def rejectRequest(request, pk):
    if request.method == "POST":
        promotion = Promotion.objects.get(pk=pk)
        promotion.status = Promotion.STATUS_REJECTED
        promotion.save()
    return redirect("promotion_detail", pk=pk)


def deleteElection(request, pk):
    if request.method == "POST":
        election = models.Election.objects.get(pk=pk)
        election.delete()
        return redirect("elections/register")
