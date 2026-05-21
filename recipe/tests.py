from django.test import TestCase
from django.urls import reverse
from .models import Category, Recipe

class RecipeViewsTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Тестова категорія")
        
        for i in range(6):
            Recipe.objects.create(
                title=f"Рецепт №{i}",
                description=f"Опис тестового рецепта {i}",
                instructions="Крок 1. Крок 2.",
                ingredients="Тестові інгредієнти",
                category=self.category
            )

   