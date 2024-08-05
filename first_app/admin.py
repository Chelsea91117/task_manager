from django.contrib import admin
from first_app.models import *


class SubTaskInline(admin.StackedInline):
    model = SubTask
    extra = 1


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'status', 'deadline', 'created_at')
    search_fields = ('title', )
    list_filter = ('categories', 'status')
    ordering = ('deadline', )
    list_per_page = 5
    inlines = [SubTaskInline]


@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'task', 'status', 'deadline', 'created_at')
    search_fields = ('title', )
    list_filter = ('task', 'status')
    ordering = ('deadline', )
    list_per_page = 5


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    ordering = ('name',)




