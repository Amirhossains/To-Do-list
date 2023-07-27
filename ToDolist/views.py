# from django.http import Http404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Users, Tasks
from .serializers import TasksListSerializer, TasksDetailSerializer, UsersListSerializer, UsersDetailSerializer


class TasksListView(APIView):

    def get(self, request):
        tasks = Tasks.objects.all()
        serializer = TasksListSerializer(tasks, many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TasksDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TasksDetailView(APIView):

    def get(self, request, pk):
        try:
            task = Tasks.objects.get(pk=pk)
        except Tasks.DoesNotExist:
            return Response(data={'detail': '404 error'})
        serializer = TasksDetailSerializer(task, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        try:
            task = Tasks.objects.get(pk=pk)
        except Tasks.DoesNotExist:
            return Response(data={'detail': '404 error'})
        serializer = TasksDetailSerializer(task, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            task = Tasks.objects.get(pk=pk)
        except Tasks.DoesNotExist:
            return Response(data={'detail': '404 error'})
        task.delete()
        return Response(data={'detail': 'task deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)


class UsersListView(APIView):

    def get(self, request):
        users = Users.objects.all()
        serializer = UsersListSerializer(users, many=True, context=({'request': request}))
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UsersDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsersDetailView(APIView):

    def get(self, request, pk):
        try:
            user = Users.objects.get(pk=pk)
        except Users.DoesNotExist:
            return Response(data={'detail': '404 error'})
        serializer = UsersDetailSerializer(user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        try:
            user = Users.objects.get(pk=pk)
        except Users.DoesNotExist:
            return Response(data={'detail': '404 error'})
        serializer = UsersDetailSerializer(user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            user = Users.objects.get(pk=pk)
        except Users.DoesNotExist:
            return Response(data={'detail': '404 error'})
        user.delete()
        return Response(data={'detail': 'The user deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
