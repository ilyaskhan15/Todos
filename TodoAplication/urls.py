from django.urls import path, include
from .views import TodosViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', TodosViewSet, basename='todos')


urlpatterns = [
    path('', include(router.urls)),
]