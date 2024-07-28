
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User, Task


class TaskTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.task = Task.objects.create(title='Test Task', user=self.user)

    def test_create_task(self):
        url = reverse('task-list')
        data = {'title': 'New Task'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_tasks(self):
        url = reverse('task-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_task_detail(self):
        url = reverse('task-detail', args=[self.task.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_task(self):
        url = reverse('task-detail', args=[self.task.id])
        data = {'title': 'Updated Task'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_task(self):
        url = reverse('task-detail', args=[self.task.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
