from django.contrib import admin

from .models import Option, Student, Message, UserRiddle, Mark

admin.site.register(Student)
admin.site.register(Option)
admin.site.register(Message)
admin.site.register(UserRiddle)
admin.site.register(Mark)