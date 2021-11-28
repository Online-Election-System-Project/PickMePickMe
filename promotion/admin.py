from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Promotion)
class Promotion(admin.ModelAdmin):

    list_display = (
        "title",
        "content",
        "poster",
        "candidate",
        "election"
    ) 
    