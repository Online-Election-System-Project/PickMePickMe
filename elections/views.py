from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import cv2
import threading
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import ListView, FormView, UpdateView
from django.urls import reverse_lazy, reverse
from django.views.generic.detail import DetailView

from . import forms, models

from promotion import models as promotions_model


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


def deleteElection(request, pk):
    if request.method == "POST":
        election = models.Election.objects.get(pk=pk)
        election.delete()
        return redirect("elections/register")


class ElectionResultView(DetailView):

    """ElectionResultView Definition"""

    def get(self, request, pk):
        try:
            election = models.Election.objects.get(pk=pk)
        except models.Election.DoesNotExist:
            raise Http404()

        return render(
            request,
            "elections/election_result.html",
            {"election": election, "elected": "문재인"},
        )


class VoteView(FormView):
    """
    Vote View
    """

    def get(self, request, pk):
        try:
            election = models.Election.objects.get(pk=pk)
            promotions = promotions_model.Promotion.objects.filter(election=election.id)
        except models.Election.DoesNotExist:
            raise Http404()
        return render(
            request,
            "elections/vote.html",
            {"election": election, "promotions": promotions},
        )


def Calculate(request, pk):
    election = models.Election.objects.get(pk=pk)
    promotions = promotions_model.Promotion.objects.filter(election=election.id)
    try:
        selected_choice = promotions.get(name_kor=request.POST["choice"])
    except (KeyError,):
        return render(
            request,
            "elections/vote.html",
            {"election": election, "promotions": promotions},
        )
    else:
        selected_choice.vote_number += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("elections:done-voting"))


def CertificationView(request, pk):
    election = models.Election.objects.get(pk=pk)
    promotions = promotions_model.Promotion.objects.filter(election=election.id)
    if request.method == "POST":
        return render(
            request,
            "elections/vote.html",
            {"election": election, "promotions": promotions},
        )
    else:
        return render(request, "elections/certification.html", {"election": election})


def CertificationAgentView(request, pk):
    context = {
        "pk": pk,
    }
    return render(request, "elections/certification_forAgent.html", context)


def DoneVoting(request):
    context = {}
    return render(request, "elections/vote-done.html", context)


class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode(".jpg", image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n\r\n")


@gzip.gzip_page
def VideoRecord(request):
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(
            gen(cam), content_type="multipart/x-mixed-replace;boundary=frame"
        )
    except:  # This is bad! replace it with proper handling
        print("에러입니다...")
        pass
