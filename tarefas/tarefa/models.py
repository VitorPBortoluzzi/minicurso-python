from django.db import models
from django.urls import reverse


class Categoria(models.Model):
    nome = models.CharField('Nome', max_length=20)

    def __str__(self):
        return self.nome


class Tarefa(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    descricao = models.CharField('Descrição', max_length=100)
    obs = models.TextField('Observações', null=True, blank=True)
    realizada = models.BooleanField('Realizada', default=False)

    def get_absolute_url(self):
        return reverse('tarefa_update', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('tarefa_delete', kwargs={'pk': self.id})