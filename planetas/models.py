from django.db import models


class Planeta(models.Model):
    class Meta:
        db_table = 'planeta'

    nome = models.CharField(max_length=200, unique=True)
    clima = models.CharField(max_length=2, choices=[('CO', 'Congelado'), ('TR', 'Tropical'), ('TE', 'Temperado'),
                                                    ('AR', 'Árido')])
    terreno = models.CharField(max_length=200, choices=[('DE', 'Deserto'), ('OC', 'Oceano'), ('FL', 'Florestas'),
                                                        ('MO', 'Montanhoso'), ('TU', 'Tundra'), ('PA', 'Pantano')])

    def __str__(self):
        return self.nome
