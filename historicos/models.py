from django.db import models
from django.db.models import CharField
from agendamentos.models import Agendamentos


# Create your models here.

class Historico(models.Model):
    id_historico = models.AutoField(primary_key=True)
    data = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    aparacimentos_sintomas = models.CharField(max_length=100, blank=True, null=True)
    duracao_sintomas = CharField(max_length=100, blank=True, null=True)
    local_dor = CharField(max_length=100, blank=True, null=True)
    tipo_dor = CharField(max_length=100, blank=True, null=True)
    conclusao = models.TextField(max_length=100, blank=True, null=True)

    # Relações
    id_agendamento = models.ForeignKey(Agendamentos, related_name='historicos', on_delete=models.CASCADE)


    class Meta:
        managed=True
        db_table = 'historicos'
