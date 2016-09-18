# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Message(models.Model):
    msg_id = models.IntegerField()
