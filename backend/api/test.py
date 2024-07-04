from load.models import Load

# Пример QuerySet
queryset = Load.objects.all()

# Получение SQL запроса
sql_query = str(queryset.query)
print(sql_query)
