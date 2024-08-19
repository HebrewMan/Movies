from django.shortcuts import render
from django.http import JsonResponse,Http404
from rest_framework.decorators import api_view
from rest_framework import status,generics,viewsets
from rest_framework.response import Response

from rest_framework import mixins

from rest_framework.views import APIView

from .models import Movie,Category
from .serializers import MovieSerializer,CategorySerializer
from rest_framework.permissions import IsAdminUser
# from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters


# Create your views here.
# @api_view(['GET','POST'])

# class MovieList(generics.ListCreateAPIView):
#     queryset = Movie.objects.all() 
#     serializer_class = MovieListSerializer
    
# class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Movie.objects.all()
    
#     serializer_class = MovieListSerializer

# api/movie


class MovieFilter(filters.FilterSet):
    movie_name = filters.CharFilter(lookup_expr='icontains')
    category_id = filters.NumberFilter()
    region = filters.NumberFilter()

    class Meta:
        model = Movie
        fields = ['movie_name', 'category_id', 'region'] 


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    # filterset_fields = ('movie_name',)
    filterset_class = MovieFilter
        

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [IsAdminUser]


