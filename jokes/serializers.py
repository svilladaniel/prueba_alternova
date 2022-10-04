# DRF
from rest_framework import serializers

# Models
from jokes.models import MyJokes


class MyJokesModelSerializer(serializers.ModelSerializer):
    ''''''

    class Meta:
        model = MyJokes
        # exclude = []
        # read_only_fields = []