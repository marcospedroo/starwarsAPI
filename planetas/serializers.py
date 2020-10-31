from rest_framework import serializers
from .models import Planeta
import requests


class PlanetaSerializer(serializers.ModelSerializer):
    filmes = serializers.SerializerMethodField()

    class Meta:
        model = Planeta
        fields = '__all__'

    def get_filmes(self, obj):
        url = 'https://swapi.dev/api/planets/'
        params = {'search': obj.nome}
        r = requests.get(url=url, params=params)
        planetas = r.json()
        quantidade_filmes = 0
        if planetas['results']:
            quantidade_filmes = len(planetas['results'][0]['films'])
            # for planeta in planetas['results'][0]['films']:
            #     quantidade_filmes += 1
        
        return quantidade_filmes