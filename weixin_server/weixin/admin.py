# -*- coding: utf-8 -*-
from django.contrib import admin
from weixin.models import *
# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    list_display = ('msg_id',)
admin.site.register(Message,MessageAdmin)