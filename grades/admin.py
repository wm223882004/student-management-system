from django.contrib import admin
from .models import Grade

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'score', 'created_at')
    list_filter = ('course',)
    search_fields = ('student__name', 'student__student_id', 'course__name')
    ordering = ('-created_at',)
