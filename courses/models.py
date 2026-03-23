from django.db import models
from teachers.models import Teacher

class Course(models.Model):
    course_id = models.CharField(max_length=20, unique=True, verbose_name='课程编号')
    name = models.CharField(max_length=100, verbose_name='课程名称')
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='任课教师')
    credit = models.PositiveIntegerField(verbose_name='学分')
    semester = models.CharField(max_length=20, verbose_name='学期')
    description = models.TextField(blank=True, verbose_name='课程描述')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = '课程'
        db_table = 'courses'

    def __str__(self):
        return f"{self.name} ({self.course_id})"
