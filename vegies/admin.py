from django.contrib import admin

# Register your models here.
from .models import *

class RecipeUser(admin.ModelAdmin):
    list_display = ("recipe_name",  "user",)

admin.site.register(Recipe, RecipeUser)