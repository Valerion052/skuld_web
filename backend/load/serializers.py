from rest_framework import serializers
from .models import Load

class LoadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Load
        fields = ('ds', 'business_line', 'sector', 'skill_group',
                  'channel', 'transactions', 'aht', 'asa', 'interval', 
                  'shrinkage', 'version')