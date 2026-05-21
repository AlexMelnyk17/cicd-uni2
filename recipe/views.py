from django.shortcuts import render
from .models import Recipe

def main(request):
    latest_recipes = Recipe.objects.all().order_by('-created_at')[:5]
    return render(request, "main.html", {'recipes': latest_recipes})
