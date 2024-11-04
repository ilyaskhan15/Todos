from django.urls import path
from .views import todos_list,todos_detail


urlpatterns = [
    path('', todos_list),
    path('<pk>/', todos_detail),
]