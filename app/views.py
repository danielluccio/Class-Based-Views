from django.shortcuts import render
from .models import Tarefa, Categoria
from django.views.generic import ListView



class TarefaListView(ListView):
    model = Tarefa
    template_name = 'tarefa_list.html'

