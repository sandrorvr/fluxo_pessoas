from rest_framework import serializers
from chart.models import fluxo

class fluxoSerializers(serializers.ModelSerializer):
    class Meta:
        model = fluxo
        fields = [
            'cod_pes',
            'sent_pes',
            'time_pes',
            'total_pes',
            'date_pes'
        ]