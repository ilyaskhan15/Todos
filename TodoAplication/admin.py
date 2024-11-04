from django.contrib import admin
from .models import Todos


class TodosAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'description', 'due_date', 'created_at', 'priority', 'completed','user_id')
    search_fields = ('title', 'description')
    list_filter = ('priority', 'completed')
    list_per_page =  10

admin.site.register(Todos, TodosAdmin)