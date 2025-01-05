from rest_framework import viewsets

from imagens.models import ImagemHistorico
from imagens.api.serializers import ImagensHistoricoSerializer

class ImagensHistoricoViewSets(viewsets.ModelViewSet):
    queryset = ImagemHistorico.objects.all()
    serializer_class = ImagensHistoricoSerializer
