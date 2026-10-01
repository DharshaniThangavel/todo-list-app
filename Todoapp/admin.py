from django.contrib import admin
#adding the model to admin.py
from Todoapp.models import Todo

# Register your models here.
admin.site.register(Todo)