from rest_framework import serializers

from .models import Tasks, Users


class TasksListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tasks
        fields = ['id', 'user', 'title', 'is_done', 'url']


class TasksDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['id', 'user', 'title', 'description', 'finishing_time', 'is_done']


class UsersListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'name', 'email', 'is_active', 'url']


class UsersDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'name', 'nickname', 'email', 'password', 'is_active']
