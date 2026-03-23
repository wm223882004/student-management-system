from django.db import models
from users.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    student_id = models.CharField(max_length=20, unique=True, verbose_name='学号')
    name = models.CharField(max_length=50, verbose_name='姓名')
    GENDER_CHOICES = (
        ('M', '男'),
        ('F', '女'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name='性别')
    age = models.PositiveIntegerField(verbose_name='年龄')
    major = models.CharField(max_length=100, verbose_name='专业')
    enrollment_year = models.PositiveIntegerField(verbose_name='入学年份')
    phone = models.CharField(max_length=11, blank=True, verbose_name='电话')
    email = models.EmailField(blank=True, verbose_name='邮箱')
    address = models.TextField(blank=True, verbose_name='地址')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = '学生'
        verbose_name_plural = '学生'
        db_table = 'students'

    def __str__(self):
        return f"{self.name} ({self.student_id})"
