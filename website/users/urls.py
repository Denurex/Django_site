from django.urls import path
from . import views
from django.contrib.auth import views as authViews

urlpatterns = [
    path("signup/", views.register, name="signup_page"),
    path("signin/", views.login_view, name="auth_page"),
    path("logout/", views.logout_view, name="logout_page"),
    path("profile/<int:id>/", views.check_profile, name="profile_page"),
    # path("signin/", authViews.LoginView.as_view(template_name="users/signin.html"), name="auth_page"),
]
