from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'name', 'teacher', 'credit', 'semester', 'created_at')
    list_filter = ('semester', 'credit')
    search_fields = ('course_id', 'name', 'teacher__name')
    ordering = ('-created_at',)
