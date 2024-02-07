from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .serializers import TodoSerializer
from .models import Todo
'''
@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        # Generate token or session here
        return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
'''
    

@api_view(['GET'])
def todo_list(request): 
    if request.method == 'GET':
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def todo_post(request):
    if request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
def todo_delete(request):    
    if request.method == 'DELETE':
        todo_id = request.data.get('id')
        try:
            todo = Todo.objects.get(id=todo_id)
            todo.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Todo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        

@api_view(['PATCH'])        
def todo_update(request):    
    if request.method == 'PATCH':
        todo_id = request.data.get('id')
        is_done = request.data.get('is_done')
        try:
            todo = Todo.objects.get(id=todo_id)
            todo.is_done = is_done
            todo.save()
            serializer = TodoSerializer(todo)
            return Response(serializer.data)
        except Todo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
@api_view(['DELETE'])
def todo_delete_all(request):    
    if request.method == 'DELETE':
            todos = Todo.objects.all()
            todos.delete()


    
        
    
        