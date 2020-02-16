
from .models import Author
from rest_framework import  serializers

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'short_description']