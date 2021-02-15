from rest_framework import serializers
from .models import *

class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = ['id', 'url', 'name', 'paradign']

class ParadignSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paradign
        fields = ['id', 'url', 'name']

class ProgrammerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Programmer
        fields = ['id', 'url', 'name', 'languages']