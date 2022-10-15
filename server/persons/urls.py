from django.urls import path

from persons import views

urlpatterns = [
    path("", views.add_new_person, name="add-persons"),
]
