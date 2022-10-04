# Import Django modules
from django.urls import include, path

# Import Django rest framework modules
from rest_framework import routers
from rest_framework.routers import DefaultRouter

# Import Views
from .views import MyJokesViewSet, JokesManagement, FavoriteJokes


router = DefaultRouter()


router.register(r'my-jokes', MyJokesViewSet, basename='My-jokes')

urlpatterns = [
    path('', include(router.urls)),
    path('show-chucknorris-jokes', JokesManagement.as_view()),
    path('save-favorite-jokes/<str:joke_id>', FavoriteJokes.as_view())
]