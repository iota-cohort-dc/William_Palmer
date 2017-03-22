from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    first_name: model.CharField(max_length = 255)
    last_name: model.CharField(max_length = 255)
    email: model.CharField(max_length = 255)
    password: model.CharField(max_length = 255)
    created_at: model.DateTimeField(auto_add_now=True)
    updated_at: model.DateTimeField(auto_now=True)

class Message(models.Model):
    message: model.TextField(max_length = 1000)
    user_id: = model.ForeignKey(User)
    created_at: model.DateTimeField(auto_add_now=True)
    updated_at: model.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment: = model.TextField(max_length=1000)
    message_id: model.ForeignKey(Message)
    user_id: = model.ForeignKey(User)
    created_at: model.DateTimeField(auto_add_now=True)
    updated_at: model.DateTimeField(auto_now=True)
