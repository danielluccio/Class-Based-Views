from django.urls import path
from .views import TarefaListView


urlpatterns = [
    path('listar/', TarefaListView.as_view(), name='tarefa_list')
]