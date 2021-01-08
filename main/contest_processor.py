from .models import Category
from django.shortcuts import render
from django.urls import path

def get_categories(request):
    categories = Category.objects.filter(parent__isnull=True)
    return {'categories': categories}
