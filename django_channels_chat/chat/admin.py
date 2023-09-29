from django.contrib import admin
from .models import Event, Message, Group


admin.site.register(Message)
admin.site.register(Event)
admin.site.register(Group)
