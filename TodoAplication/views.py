from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Todos
from .serializers import TodosSerializer

@api_view(['GET', 'POST'])
def todos_list(request):
    if request.method == 'GET':
        query_set = Todos.objects.filter(user=request.user)
        serializer = TodosSerializer(query_set, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TodosSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Associate the todo with the authenticated user
        todos = serializer.save(user=request.user)
        return Response(TodosSerializer(todos).data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT', 'DELETE'])
def todos_detail(request, pk):
    todos = get_object_or_404(Todos,pk=pk)
    if request.method == "GET":
        serializer = TodosSerializer(todos)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TodosSerializer(todos, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        todos.delete()
        return Response('ok', status=status.HTTP_204_NO_CONTENT)




# Create your views here.
