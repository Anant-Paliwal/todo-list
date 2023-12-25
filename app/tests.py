from django.test import TestCase
from .models import TodoItem
from django.utils import timezone
import datetime

class TodoItemModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        TodoItem.objects.create(title='Test Todo', description='Test Description')

    def test_title_content(self):
        todo = TodoItem.objects.get(id=1)
        expected_object_name = f'{todo.title}'
        self.assertEquals(expected_object_name, 'Test Todo')

    def test_description_content(self):
        todo = TodoItem.objects.get(id=1)
        expected_object_description = f'{todo.description}'
        self.assertEquals(expected_object_description, 'Test Description')

    def test_due_date_optional(self):
        todo = TodoItem.objects.get(id=1)
        self.assertTrue(todo.due_date is None or isinstance(todo.due_date, datetime.date))

    def test_status_default_open(self):
        todo = TodoItem.objects.get(id=1)
        self.assertEquals(todo.status, 'OPEN')


