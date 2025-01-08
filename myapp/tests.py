from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Block
from .forms import BlockForm


class BlockViewTests(TestCase):

    def setUp(self):
        # Создаем несколько блоков для тестов
        self.block1 = Block.objects.create(name="Block 1")
        self.block2 = Block.objects.create(name="Block 2")

    def test_index_view(self):
        # Проверяем, что страница index загружается
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Block 1')
        self.assertContains(response, 'Block 2')

    def test_list_view(self):
        # Проверяем, что страница list загружается
        response = self.client.get(reverse('list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Block 1')
        self.assertContains(response, 'Block 2')

    def test_create_view_post(self):
        # Проверяем создание нового блока через POST-запрос
        data = {'name': 'Block 3'}
        response = self.client.post(reverse('create'), data)
        self.assertEqual(response.status_code, 302)  # Redirection
        self.assertEqual(Block.objects.count(), 3)
        self.assertRedirects(response, reverse('list'))

    def test_create_view_get(self):
        # Проверяем, что форма отображается для создания нового блока
        response = self.client.get(reverse('create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'form.html')

    def test_update_view_post(self):
        # Проверяем, что блок можно обновить
        data = {'name': 'Updated Block'}
        response = self.client.post(reverse('update', args=[self.block1.id]), data)
        self.block1.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.block1.name, 'Updated Block')
        self.assertRedirects(response, reverse('list'))

    def test_update_view_get(self):
        # Проверяем, что форма отображается для обновления блока
        response = self.client.get(reverse('update', args=[self.block1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'form.html')

    def test_delete_view(self):
        # Проверяем, что блок удаляется
        response = self.client.get(reverse('delete', args=[self.block1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Block.objects.count(), 1)
        self.assertNotContains(response, 'Block 1')
