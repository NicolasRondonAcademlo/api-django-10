import imp
from .views import list_publications, PublicationsList, PublicationViewset
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'publications/crud', PublicationViewset)


urlpatterns = [
    path('publications/', list_publications),
    path('publications_list_api_view/', PublicationsList.as_view()),
] + router.urls