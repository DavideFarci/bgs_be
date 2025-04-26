from django.db import models
from django.contrib.auth.models import User  

class Game(models.Model):
    nome = models.CharField(max_length=255)
    descrizione = models.TextField(blank=True, null=True)
    anno_di_pubblicazione = models.IntegerField(blank=True, null=True)
    categorie = models.CharField(max_length=255, blank=True, null=True)
    autori = models.CharField(max_length=255, blank=True, null=True)
    artisti = models.CharField(max_length=255, blank=True, null=True)
    min_giocatori = models.IntegerField()
    max_giocatori = models.IntegerField()
    tempo_di_gioco = models.CharField(max_length=255, blank=True, null=True)
    immagine = models.CharField(max_length=255, blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='games')

    def get_params(self):
        return [param.nome for param in self.params.all()]

class GameParam(models.Model):
    game = models.ForeignKey(Game, related_name='params', on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
