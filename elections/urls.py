from django.urls import path
from . import views

app_name = "elections"

urlpatterns = [
    path("", views.ElectionListView.as_view(), name="elections"),
    path("<int:pk>/", views.ElectionDetailView.as_view(), name="detail"),
    path(
        "register/",
        views.ElectionRegisterView.as_view(),
        name="election-register",
    ),
    path("<int:pk>/certification/", views.CertificationView, name="certification"),
    path(
        "<int:pk>/certification_for_agent/",
        views.CertificationAgentView,
        name="certification-for-agent",
    ),
    path("videorecord/", views.VideoRecord, name="video-record"),
    path("done-voting/", views.DoneVoting, name="done-voting"),
    path("<int:pk>/vote/", views.VoteView.as_view(), name="vote"),
    path("<int:pk>/calculate/", views.Calculate, name="calculate"),
    path("<int:pk>/edit/", views.EditElectionView.as_view(), name="edit-election"),
    path("<int:pk>/delete/", views.deleteElection, name="delete-election"),
    path("<int:pk>/result/", views.ElectionResultView.as_view(), name="result"),
]
