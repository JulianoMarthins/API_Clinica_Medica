from rest_framework import serializers

from agendamentos.models import Agendamentos
from historicos.api.serializers import HistoricosSerializers


class AgendamentosSerializers(serializers.ModelSerializer):

    class Meta:
        model = Agendamentos
        fields = '__all__'



class AgendamentosDetalhesSerializers(serializers.ModelSerializer):
    historicos = HistoricosSerializers(many=True, read_only=True)

    class Meta:
        model = Agendamentos
        fields = [
            'id_agendamento',
            'data_hora',
            'data_agendamento',
            'cancelado',
            'obs',
            'tipo',
            'historicos'
        ]