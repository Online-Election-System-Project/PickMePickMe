from django.shortcuts import render
from django.views.generic import FormView, ListView
from django.urls import reverse_lazy
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import cv2
import threading
from . import forms

# Create your views here.


class ElectionRegisterView(FormView):
    template_name = "elections/register.html"
    form_class = forms.ElectionRegisterForm
    success_url = reverse_lazy("elections:election-register")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class VoteView(FormView):
    """
    Vote View
    """

    template_name = "elections/vote.html"
    form_class = forms.ElectionRegisterForm
    success_url = reverse_lazy("elections:vote")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def CertificationView(request):
    context = {}

    return render(request, "elections/certification.html", context)


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
