from django.contrib import admin
from .models import RecipeModel, CategoryModel


admin.site.register(RecipeModel) 
admin.site.register(CategoryModel)
