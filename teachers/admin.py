from django.contrib import admin
from .models import Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('teacher_id', 'name', 'title', 'department', 'phone', 'email', 'created_at')
    list_filter = ('title', 'department')
    search_fields = ('teacher_id', 'name', 'department')
    ordering = ('-created_at',)
