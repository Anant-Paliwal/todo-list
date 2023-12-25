from django.contrib import admin
from .models import TodoItem

@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp', 'due_date', 'status']
    list_filter = ['status', 'due_date']
    search_fields = ['title', 'description', 'tags']

    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'due_date', 'tags', 'status')
        }),
    )

    readonly_fields = ['timestamp']
