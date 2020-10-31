from django.db import models


class Planeta(models.Model):

    class Meta:
        db_table = 'planeta'

    nome = models.CharField(max_length=200)
    clima = models.CharField(max_length=200)
    terreno = models.CharField(max_length=200)

    def __str__(self):
        return self.title
