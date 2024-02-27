from django.urls import path

from .views import (UserLoginView, add_recipe, edit_recipe, logout_view, register, full_recipe, category_recipes,
                    complexity_recipes, author_recipes, random_recipe, index)

urlpatterns = [
    path('', index, name='index'),
    path('random/', random_recipe, name='random_recipe'),
    path('full_recipe/<int:recipe_id>/', full_recipe, name='full_recipe'),
    path('category_recipes/<slug:category_name>/', category_recipes, name='category_recipes'),
    path('complexity_recipes/<slug:complexity_rate>/', complexity_recipes, name='complexity_recipes'),
    path('author_recipes/<int:author_id>/', author_recipes, name='author_recipes'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_view, name='logout'),
    path('add_recipe/', add_recipe, name='add_recipe'),
    path('edit_recipe/<int:recipe_id>/', edit_recipe, name='edit_recipe')
]
