import json
from django.http import JsonResponse
from django.shortcuts import render
from .models import Publication
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .serializers import PublicationSerializer, CreatePublicationSerializer
from rest_framework import viewsets

@api_view(['POST', "GET"])
def list_publications(request):
    if request.method == 'POST':
        data = request.data
        if "title" not in data:
            return Response({"message": "Title is required"}, status=status.HTTP_400_BAD_REQUEST)
        new_publication =Publication.objects.create(title=data["title"])
        return Response({"message": "Publication created successfully", "data": {
            "publication": {
                "id": new_publication.id,
                "title": new_publication.title
            }
        }}, 
        status=status.HTTP_201_CREATED)
    publications = Publication.objects.all()
    count = publications.count()
    publications = [
            {"id": publication.id,  "title": publication.title} 
            for publication in publications
            ]
    return Response({
            "data": {
                "count": count,
                "publications": publications
            }
        })

class PublicationsList(generics.ListCreateAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer

    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = PublicationSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CreatePublicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PublicationViewset(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer