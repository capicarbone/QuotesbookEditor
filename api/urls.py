from django.urls import include, path
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'authors', AuthorsListView.as_view(), basename='authors' )

urlpatterns = [
    #path('', include(router.urls)),
    path(r'authors', AuthorsListView.as_view()),
    path(r'quotes', QuotesListView.as_view()),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]