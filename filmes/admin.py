from django.contrib import admin
from .models import Generos, Filmes
from rest_framework.authtoken.models import Token

# Admin para o modelo Generos: mostra o campo 'nome' e permite busca por nome
@admin.register(Generos)
class GenerosAdmin(admin.ModelAdmin):
   list_display = ['nome']
   search_fields = ["nome"]


@admin.register(Filmes)
class FilmeAdmin(admin.ModelAdmin):
  list_display = ['titulo', 'descricao', 'ano_lancamento', 'genero', 'duracao']     
  search_fields = ['titulo', 'descricao', 'genero']
  list_filter = ['ano_lancamento', 'duracao']

admin.site.register(Token)
