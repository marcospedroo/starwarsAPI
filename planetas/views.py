from django.shortcuts import render
from django_filters import rest_framework as filters
from rest_framework import generics

from planetas.models import Planeta
from planetas.serializers import PlanetaSerializer


class PlanetaList(generics.ListCreateAPIView):
    queryset = Planeta.objects.all()
    serializer_class = PlanetaSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'


class PlanetaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Planeta.objects.all()
    serializer_class = PlanetaSerializer
