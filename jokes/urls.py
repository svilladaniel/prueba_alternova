# Import Django modules
from django.urls import include, path

# Import Django rest framework modules
from rest_framework import routers
from rest_framework.routers import DefaultRouter

# Import Views
from .views import OwnJokesViewSet, ChuckNorrysJokesViewSet


router = DefaultRouter()


router.register(r'chuk-norrys-jokes', ChuckNorrysJokesViewSet, basename='chuk-norrys-jokes')
router.register(r'own-jokes', OwnJokesViewSet, basename='own-jokes')

urlpatterns = [
    path('', include(router.urls))
]