from rest_framework import viewsets
from load.models import Load
from load.serializers import LoadSerializer

class LoadViewSet(viewsets.ModelViewSet):
    queryset = Load.objects.using('DWH').all()
    sql_query = str(queryset.query)
    print(sql_query)
    serializer_class = LoadSerializer