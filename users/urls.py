from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path(
        "login/",
        views.LoginView.as_view(),
        name="login",
    ),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("update-profile/", views.UpdateProfileView.as_view(), name="update-profile"),
    path("delete-user/", views.deleteUser, name="delete-user"),
]
