"""
URLS Routing for main-store related pages.
"""
from django.urls import path

from store.views import index

urlpatterns = [
    path("", index.store, name="index"),
]
