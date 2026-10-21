from django.db import models

class Generos(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
       return self.nome

class Filmes(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    ano_lancamento = models.PositiveIntegerField()
    genero = models.ForeignKey(Generos, on_delete=models.CASCADE)
    duracao = models.PositiveIntegerField()

    def __str__(self):
       return self.titulo
