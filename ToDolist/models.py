from django.db import models


class Users(models.Model):
    name = models.CharField(verbose_name='name', max_length=25)
    nickname = models.CharField(verbose_name='nick name', max_length=20, blank=True, null=True)
    email = models.CharField(verbose_name='email', max_length=32, blank=True)
    password = models.CharField(verbose_name='password', max_length=12, blank=True)
    is_active = models.BooleanField(verbose_name='is active', default=True)
    created_time = models.DateTimeField(verbose_name='created time', auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name='updated time', auto_now=True)


class Tasks(models.Model):
    user = models.ForeignKey(to=Users, on_delete=models.CASCADE)
    title = models.CharField(verbose_name='title', max_length=32)
    description = models.TextField(verbose_name='description')
    finishing_time = models.DateTimeField(verbose_name='finishing time', blank=True, null=True,
                                          help_text='set a time for finishing this task')
    is_done = models.BooleanField(verbose_name='is done', default=False, help_text='Did you finish this task')
    created_at = models.DateTimeField(verbose_name='created at', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='updated at', auto_now=True)
