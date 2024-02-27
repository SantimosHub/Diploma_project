from django import forms
from .models import RecipeModel, CategoryModel, RecipeToCategoryModel
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    pass


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class RecipeForm(forms.ModelForm):
    class Meta:
        model = RecipeModel
        fields = ('title', 'description', 'cooking', 'time', 'image', 'categories', 'complexity')


class CategoryForm(forms.ModelForm):
    class Meta:
        model = CategoryModel
        fields = ('title',)


class RecipeToCategoryForm(forms.ModelForm):
    model = RecipeToCategoryModel
    fields = ()
