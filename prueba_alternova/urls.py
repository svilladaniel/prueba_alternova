"""prueba_alternova URL Configuration"""

from django.contrib import admin
from django.urls import path, include
# from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# Serializers
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('jokes-api/', include(('jokes.urls', 'jokes'), namespace='jokes-api')),
]
