from rest_framework import serializers

from pacientes.models import Pacientes
from agendamentos.api.serializers import AgendamentosSerializers


class PacientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pacientes
        fields = '__all__'



class PacientesDetalhesSerializer(serializers.ModelSerializer):
    agendamentos = AgendamentosSerializers(many=True, read_only=True)

    class Meta:
        model = Pacientes
        fields = [
            'id_paciente',
            'nome',
            'nascimento',
            'endereco',
            'num_endereco',
            'bairro',
            'cep',
            'data_cadastro',
            'rg',
            'agendamentos'
        ]