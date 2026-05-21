from django.shortcuts import render
from .models import Recipe, Category
from django.db.models import Count

def main(request):
    latest_recipes = Recipe.objects.all().order_by('-created_at')[:5]
    return render(request, "main.html", {'recipes': latest_recipes})

def category_list(request):
    categories = Category.objects.annotate(recipe_count=Count('categories'))
    return render(request, "category_list.html", {'categories': categories})