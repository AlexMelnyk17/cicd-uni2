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

    def test_main_view_status_and_limit(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        
        self.assertTemplateUsed(response, 'main.html')
        
        self.assertEqual(len(response.context['recipes']), 5)

    def test_category_list_view_status_and_count(self):
        response = self.client.get(reverse('category_list'))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category_list.html')
        
        first_category = response.context['categories'].first()
        self.assertEqual(first_category.recipe_count, 6)