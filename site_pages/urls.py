"""
URLS Routing for common static pages.
"""
from site_pages.views.common import about

from django.urls import path

urlpatterns = [path("/about", about), path('')]
