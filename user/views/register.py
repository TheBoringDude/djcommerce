"""
VIEW HANDLER FOR USER REGISTER.
"""

from django.shortcuts import render


def RegisterView(request):
    return render(request, "user_forms/register.html")