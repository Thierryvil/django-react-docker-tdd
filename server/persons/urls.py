from django.urls import path

from persons.views import PersonViews

urlpatterns = [
    path("", PersonViews.as_view(), name="persons"),
]
