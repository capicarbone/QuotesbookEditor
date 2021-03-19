from django.shortcuts import render
import random
import json
from rest_framework import generics
from rest_framework.views import APIView, Response

from .models import Author, Quote
from .serializers import AuthorSerializer, QuoteSerializer


class AuthorsListView(generics.ListAPIView):
    serializer_class = AuthorSerializer

    def get_queryset(self):
        lang = self.request.query_params.get('lang')
        return Author.objects.all().filter(lang=lang).order_by('last_name')


class QuotesListView(generics.ListAPIView):
    serializer_class = QuoteSerializer

    def get_queryset(self):
        lang = self.request.query_params.get('lang') or 'en'
        return Quote.objects.all().filter(lang=lang)


class QuotesSampleView(APIView):

    def get(self, request):
        """
        Gets a random sample of quotes

        :param request:
        :return: Quotes collection
        """

        lang = request.query_params.get('lang') or 'en'
        requested_count = request.query_params.get('count') or 25
        filter_ids = json.loads(request.query_params.get('filter_ids')) \
            if request.query_params.get('filter_ids') else []

        queryset = Quote.objects.filter(lang=lang).exclude(author__in=filter_ids).order_by('author_id')
        quotes_count = queryset.count()

        quotes_indexes = list(range(0, quotes_count - 1))
        random.shuffle(quotes_indexes)
        quotes_indexes = quotes_indexes[0:requested_count]

        quotes = []
        for index in quotes_indexes:
            quotes.append(queryset[index])

        serializer = QuoteSerializer(quotes, many=True)
        return Response(serializer.data)
        

