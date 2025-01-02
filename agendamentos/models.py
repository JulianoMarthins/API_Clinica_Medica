from django.db import models

from pacientes.models import Pacientes

# Create your models here.

class Agendamentos(models.Model):
    id_agendamento = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    data_agendamento = models.DateTimeField(auto_now_add=True)
    cancelado = models.BooleanField(default=False)
    obs = models.TextField()
    tipo = models.CharField(max_length=100)



    class Meta:
        managed = True
        db_table = 'agendamentos'
        unique_together = ('data_hora', 'id_paciente')