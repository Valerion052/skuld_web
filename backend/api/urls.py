from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import LoadViewSet


app_name = 'api'

router_v1 = DefaultRouter()

router_v1.register('load', LoadViewSet)

urlpatterns = [
    path('', include(router_v1.urls)),
    path('', include('djoser.urls')),
]
