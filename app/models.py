from django.db import models


class Categoria(models.Model):
    categoria = models.CharField(max_length=200)



class Tarefa(models.Model):
    titulo = models.CharField(max_length=250)
    descricao = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    inclusao = models.DateTimeField(auto_now_add=True)
    concluida = models.BooleanField()

    
