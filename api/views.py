from django.shortcuts import render

from rest_framework import generics

from .models import Author, Quote
from .serializers import AuthorSerializer, QuoteSerializer
# Create your views here.

class AuthorsListView(generics.ListAPIView):
    serializer_class = AuthorSerializer

    def get_queryset(self):
        lang = self.request.query_params.get('lang')
        return Author.objects.all().filter(lang=lang).order_by('last_name')


class QuotesListView(generics.ListAPIView):
    serializer_class = QuoteSerializer

    def get_queryset(self):
        lang = self.request.query_params.get('lang')
        return Quote.objects.all().filter(lang=lang)

