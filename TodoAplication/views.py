from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from .models import Todos
from .serializers import TodosSerializer


class TodosViewSet(viewsets.ModelViewSet):
    serializer_class = TodosSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only fetch todos associated with the authenticated user
        return Todos.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Associate the todo with the authenticated user upon creation
        serializer.save(user=self.request.user)

    

