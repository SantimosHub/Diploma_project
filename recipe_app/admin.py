from django.contrib import admin

from django.contrib.auth.models import User

from .models import RecipeModel, CathegoryModel

admin.site.register(RecipeModel)
admin.site.register(CathegoryModel)
