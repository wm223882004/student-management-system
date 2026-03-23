from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'name', 'gender', 'age', 'major', 'enrollment_year', 'created_at')
    list_filter = ('gender', 'major', 'enrollment_year')
    search_fields = ('student_id', 'name', 'major')
    ordering = ('-created_at',)
