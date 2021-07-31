from django.contrib import admin
from .models import MyCard

@admin.register(MyCard)
class MyCardAdmin(admin.ModelAdmin):
    list_display = ["id","name","img","date_and_time","like"]
