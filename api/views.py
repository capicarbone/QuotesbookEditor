from django.shortcuts import render
import random
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

    SAMPLE_PAGE_SIZE = 10
    QUOTES_BY_PAGE = 3

    """
        Gets a random sample of quotes.
    """
    def get(self, request, format=None):

        lang = self.request.query_params.get('lang') or 'en'
        requested_count = self.request.query_params.get('count') or 25

        queryset = Quote.objects.filter(lang=lang)
        quotes_count = queryset.count()

        available_pages = int(quotes_count / self.SAMPLE_PAGE_SIZE)

        pages_indexes = []

        # Generating pages indexes
        while (len(pages_indexes) < requested_count / self.QUOTES_BY_PAGE):

            new_index = random.randint(0, available_pages)

            if not (new_index in pages_indexes):
                pages_indexes.append(new_index)

        # Getting quotes pages
        pages = []
        for page_index in pages_indexes:
            page_start = page_index * self.SAMPLE_PAGE_SIZE
            page_end = page_start + self.SAMPLE_PAGE_SIZE

            page = queryset[page_start:page_end]
            pages.append(page)

        # Getting random quotes from pages
        quotes = []
        for page in pages:
            new_quotes = []
            page_quotes = list(page)

            while len(new_quotes) < self.QUOTES_BY_PAGE and len(page_quotes) != 0 and len(quotes) < requested_count:
                index = random.randint(0, len(page_quotes)-1)

                quote = page_quotes[index]
                new_quotes.append(quote)
                del(page_quotes[index])
                quotes.append(quote)



        serializer = QuoteSerializer(quotes, many=True)
        return Response(serializer.data)

