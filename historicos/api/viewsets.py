from rest_framework import viewsets
from historicos.api.serializers import HistoricosSerializers
from historicos.models import Historico


class HistoricoViewSet(viewsets.ModelViewSet):
    queryset = Historico.objects.all().order_by('data')
    serializer_class = HistoricosSerializers