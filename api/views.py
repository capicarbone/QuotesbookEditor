from django.shortcuts import render

from rest_framework import generics

from .models import Author
from .serializers import AuthorSerializer
# Create your views here.

class AuthorsListView(generics.ListAPIView):
    queryset = Author.objects.all().order_by('last_name')
    serializer_class = AuthorSerializer