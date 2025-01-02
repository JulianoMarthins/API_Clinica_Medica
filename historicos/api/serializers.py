from rest_framework import serializers
from historicos.models import Historico



class HistoricosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Historico
        fields = '__all__'