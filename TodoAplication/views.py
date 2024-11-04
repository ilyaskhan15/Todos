from django.shortcuts import get_object_or_404
from .models import Todos
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TodosSerializer
from rest_framework import status
from django.contrib.auth.models import User

@api_view(['GET', 'POST'])
def todos_list(request):
    if request.method == 'GET':
        query_set = Todos.objects.all()
        serializer = TodosSerializer(query_set, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        # Get `user_id` from the request data
        user_id = request.data.get("user_id")
        if not user_id:
            return Response({"error": "user_id is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Verify the user exists
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Create the todo item with the validated user
        serializer = TodosSerializer(data=request.data)
        if serializer.is_valid():
            # Save the new todo item and associate it with the user
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
def todos_detail(request, pk):
    todos = get_object_or_404(Todos,pk=pk)
    serializer = TodosSerializer(todos)
    return Response(serializer.data)



# Create your views here.
