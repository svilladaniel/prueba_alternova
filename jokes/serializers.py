# DRF
from rest_framework import serializers

# Models
from jokes.models import ChuckNorrysJokes, OwnJokes


class ChuckNorrysJokesModelSerializer(serializers.ModelSerializer):
    ''''''

    class Meta:
        model = ChuckNorrysJokes
        # exclude = []
        # read_only_fields = []


class OwnJokesModelSerializer(serializers.ModelSerializer):
    ''''''

    class Meta:
        model = OwnJokes
        # exclude = []
        # read_only_fields = []