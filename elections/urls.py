from django.urls import path
from . import views

app_name = "elections"

urlpatterns = [
    path(
        "register/",
        views.ElectionRegisterView.as_view(),
        name="election-register",
    ),
]
