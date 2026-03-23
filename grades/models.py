from django.db import models
from students.models import Student
from courses.models import Course

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='学生')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='课程')
    score = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='成绩')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = '成绩'
        verbose_name_plural = '成绩'
        db_table = 'grades'
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student.name} - {self.course.name}: {self.score}"
