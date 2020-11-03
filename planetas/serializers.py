from rest_framework import serializers
from .models import Planeta
import requests


class PlanetaSerializer(serializers.ModelSerializer):
    filmes = serializers.SerializerMethodField()

    class Meta:
        model = Planeta
        fields = '__all__'

    @staticmethod
    def get_filmes(obj):
        url = 'https://swapi.dev/api/planets/'
        params = {'search': obj.nome}
        r = requests.get(url=url, params=params)
        planetas = r.json()
        quantidade_filmes = 0
        if planetas.get('results'):
            quantidade_filmes = len(planetas.get('results')[0].get('films'))
        
        return quantidade_filmes
