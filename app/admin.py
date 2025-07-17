from django.contrib import admin
from .models import Categoria, Tarefa


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('categoria',)
    search_fields = ('categoria',)


@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'concluida', 'inclusao', 'categoria',)
    search_fields = ('titulo',)
    list_filter = ('inclusao',)

