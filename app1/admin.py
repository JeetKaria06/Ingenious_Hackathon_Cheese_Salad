from django.contrib import admin
from .models import User_table, Question
# Register your models here.

admin.site.register(User_table)
admin.site.register(Question)