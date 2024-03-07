from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *

from .models import Task, Category

@api_view(['GET'])
def get_tasks(request):
    queryset = Task.objects.all()
    serializer = TaskSerializer(queryset,many=True)
    return Response(serializer.data,status=200)

@api_view(['POST'])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data,status=201)

@api_view(['GET'])
def get_task_by_id(request,pk):
    try:
        task = Task.objects.get(id = pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data,status=200)
    except Task.DoesNotExist:
        return Response('Not Found')

@api_view(['PUT'])
def update_task(request,pk):
    try:
        task = Task.objects.get(id=pk)
        serializer = TaskSerializer(instance=task,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=200)    
    except Category.DoesNotExist:
        return Response('Not Found')
    
@api_view(['DELETE'])
def delete_task(request,pk):
    try:
        task = Task.objects.get(id = pk)
        task.delete()
        return Response('Successfully deleted',status=200)
    
    except Category.DoesNotExist:
        return Response('Not Found')

@api_view(['GET'])
def get_categories(request):
    queryset = Category.objects.all()
    serializer = CategorySerializer(queryset,many=True)
    return Response(serializer.data,status=200)

@api_view(['POST'])
def create_category(request):

    print('=================')
    print(request)
    print(request.data)
    print('=================')

    serializer = CategorySerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data,status=201)

@api_view(['GET'])
def get_category_by_id(request,pk):
    try:
        category = Category.objects.get(id = pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data,status=200)
    except Category.DoesNotExist:
        return Response('Not Found')

@api_view(['PUT'])
def update_category(request, pk):
    try:
        category = Category.objects.get(id=pk)
        serializer = CategorySerializer(instance=category,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=200)
    
    except Category.DoesNotExist:
        return Response('Not Found')

@api_view(['DELETE'])
def delete_category(request,pk):
    try:
        category = Category.objects.get(id = pk)
        category.delete()
        return Response('Successfully deleted',status=200)
    
    except Category.DoesNotExist:
        return Response('Not Found')
    
