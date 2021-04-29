"""
User URLS Routing handler.
"""

from django.urls import path
from user.views import login, register

urlpatterns = [
    path("login/", login.UserLoginView.as_view(), name="login"),
    path("create-account/new/", register.RegisterView, name="register"),
]
