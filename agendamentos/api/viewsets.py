from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from agendamentos.models import Agendamentos
from agendamentos.api.serializers import AgendamentosSerializers, AgendamentosDetalhesSerializers


class AgendamentoViewSet(viewsets.ModelViewSet):
    queryset = Agendamentos.objects.all().order_by('data_hora')
    serializer_class = AgendamentosSerializers


    @action(detail=True, methods=['get'])
    def detalhes(self, request, pk=None, *args, **kwargs):

        queryset = Agendamentos.objects.filter(pk=pk)
        self.serializer_class = AgendamentosDetalhesSerializers
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)
