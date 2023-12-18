from rest_framework import serializers
from .models import Snippetapp

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippetapp
        fields = '__all__'