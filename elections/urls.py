from django.urls import path
from . import views

app_name = "elections"

urlpatterns = [
    path(
        "register/",
        views.ElectionRegisterView.as_view(),
        name="election-register",
    ),
    path("certification/", views.CertificationView, name="certification"),
    path("videorecord/", views.VideoRecord, name="video-record"),
]
