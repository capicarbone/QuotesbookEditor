
from .models import Author, Quote
from rest_framework import  serializers

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'short_description', 'lang']


class QuoteSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Quote
        fields = ['id', 'body','author', 'lang']