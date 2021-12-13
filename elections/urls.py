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
    path("<int:pk>/edit/", views.EditElectionView.as_view(), name="edit-election"),
    path("<int:pk>/delete/", views.deleteElection, name="delete-election"),
    path("<int:pk>/accept-request", views.acceptRequest, name="accept-request"),
    path("<int:pk>/reject-request", views.rejectRequest, name="reject-request"),
]
