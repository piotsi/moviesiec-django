from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from .models import Movie
from .serializers import MovieSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 2
    max_page_size = 2  # If set, this is a numeric value indicating the maximum allowable requested page size.
    page_size_query_param = 'page_size'  # If set, this is a string value indicating the name of a query parameter that allows the client to set the page size on a per-request basis.

class MovieViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)     
    pagination_class = StandardResultsSetPagination
    queryset = Movie.objects.all().order_by('name')
    serializer_class = MovieSerializer

    # def create(self,request):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)