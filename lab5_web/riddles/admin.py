from django.contrib import admin

from .models import Option, Riddle, Message, UserRiddle

admin.site.register(Riddle)
admin.site.register(Option)
admin.site.register(Message)
admin.site.register(UserRiddle)