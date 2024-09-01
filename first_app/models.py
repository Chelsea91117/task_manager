from rest_framework.authtoken.admin import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название категории')

    class Meta:
        db_table = 'task_manager_category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Task(models.Model):
    STATUS_CHOICES = [
        ('New', 'New'),
        ('In progress', 'In progress'),
        ('Pending', 'Pending'),
        ('Blocked', 'Blocked'),
        ('Done', 'Done')
    ]
    title = models.CharField(max_length=200, unique=True, verbose_name='Название задачи')  #unique_for_date='created_at'
    description = models.TextField(blank=True, null=True, verbose_name='Описание задачи')
    categories = models.ManyToManyField('Category', related_name='tasks', verbose_name='Категории задачи')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, verbose_name='Статус задачи')
    deadline = models.DateTimeField(verbose_name='Дата и время дедлайна')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)

    class Meta:
        db_table = 'task_manager_task'
        ordering = ['-created_at']
        verbose_name = 'Task'

    def __str__(self):
        return self.title


class SubTask(models.Model):
    STATUS_CHOICES = [
        ('New', 'New'),
        ('In progress', 'In progress'),
        ('Pending', 'Pending'),
        ('Blocked', 'Blocked'),
        ('Done', 'Done')
    ]
    title = models.CharField(max_length=200, unique=True, verbose_name='Название подзадачи')
    description = models.TextField(blank=True, null=True, verbose_name='Описание подзадачи')
    task = models.ForeignKey('Task', related_name='sub_tasks', on_delete=models.CASCADE, verbose_name='Основная задача')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, verbose_name='Статус подзадачи')
    deadline = models.DateTimeField(verbose_name='Дата и время дедлайна')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subtasks', null=True, blank=True)

    class Meta:
        db_table = 'task_manager_subtask'
        ordering = ['-created_at']
        verbose_name = 'SubTask'

    def __str__(self):
        return self.title


