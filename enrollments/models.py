from django.db import models
from students.models import Student
from courses.models import Course

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='学生')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='课程')
    enrolled_at = models.DateTimeField(auto_now_add=True, verbose_name='选课时间')

    class Meta:
        verbose_name = '选课'
        verbose_name_plural = '选课'
        db_table = 'enrollments'
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student.name} - {self.course.name}"
