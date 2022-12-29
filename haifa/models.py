# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Create your models here.
from django.contrib.auth.models import User
from django.db import models

#from django.contrib.auth import get_user_model

#User = get_user_model()
# Use the custom User model
#user = User.objects.create(username='myuser', name='My Name')



class CustomUser(User):
    name = models.CharField(max_length=50)
