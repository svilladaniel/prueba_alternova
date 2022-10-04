from django.shortcuts import render
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny

from jokes.models import ChuckNorrysJokes, OwnJokes
from rest_framework import viewsets
from jokes.serializers import ChuckNorrysJokesModelSerializer, OwnJokesModelSerializer
# Create your views here.

class ChuckNorrysJokesViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ChuckNorrysJokes.objects.all()
    serializer_class = ChuckNorrysJokesModelSerializer

class OwnJokesViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = OwnJokes.objects.all()
    serializer_class = OwnJokesModelSerializer

