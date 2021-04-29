"""
VIEW HANDLER FOR USER LOGIN
"""

from django.contrib.auth.views import LoginView
from django.shortcuts import render


class UserLoginView(LoginView):
    """
    User Login
    """

    template_name = "user_forms/login.html"