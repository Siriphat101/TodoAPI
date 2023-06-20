# from django.shortcuts import render
# from rest_framework import generics
# from .serializers import *
# from .models import *
# # Create your views here.
# class CreateTodo(generics.CreateAPIView):
#     queryset = ToDo.objects.all()
#     serializer_class = ToDoSerializer 
    
# class ListTodo(generics.ListAPIView):
#     queryset = ToDo.objects.all()
#     serializer_class = ToDoSerializer
    
# class DetailTodo(generics.RetrieveUpdateAPIView):
#     queryset = ToDo.objects.all()
#     serializer_class = ToDoSerializer
    
# class DeleteTodo(generics.DeleteAPIView):
#     queryset = ToDo.objects.all()
#     serializer_class = ToDoSerializer

from rest_framework import generics
from .serializers import ToDoSerializer
from .models import ToDo


class CreateTodo(generics.CreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    

class ListTodo(generics.ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class DetailTodo(generics.RetrieveUpdateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class DeleteTodo(generics.DestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
