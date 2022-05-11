import imp
from .views import list_publications, PublicationsList
from django.urls import path

urlpatterns = [
    path('publications/', list_publications),
    path('publications_list_api_view/', PublicationsList.as_view()),
]