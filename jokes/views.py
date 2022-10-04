from django.shortcuts import render
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny

import requests
import json

from jokes.models import MyJokes
from rest_framework import viewsets, status
from jokes.serializers import MyJokesModelSerializer

from jokes.models import MyJokes

from rest_framework.views import APIView

from rest_framework.response import Response
# Create your views here.


class MyJokesViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = MyJokes.objects.all()
    serializer_class = MyJokesModelSerializer

class JokesManagement(APIView):

    permission_classes = [AllowAny]

    def get(self, request):
        response = requests.get("https://api.chucknorris.io/jokes/random")
        respone_json = json.loads(response.content)
        return Response(respone_json)


class FavoriteJokes(APIView):

    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        response = requests.get("https://api.chucknorris.io/jokes/" + kwargs["joke_id"])
        respone_json = json.loads(response.content)

        savejokes = MyJokes.objects.create(
            value = respone_json["value"]
        )
        return Response(status=status.HTTP_201_CREATED)
