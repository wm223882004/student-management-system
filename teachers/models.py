from django.db import models
from users.models import User

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile')
    teacher_id = models.CharField(max_length=20, unique=True, verbose_name='教师编号')
    name = models.CharField(max_length=50, verbose_name='姓名')
    title = models.CharField(max_length=50, blank=True, verbose_name='职称')
    department = models.CharField(max_length=100, verbose_name='所属院系')
    phone = models.CharField(max_length=11, blank=True, verbose_name='电话')
    email = models.EmailField(blank=True, verbose_name='邮箱')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '教师'
        verbose_name_plural = '教师'
        db_table = 'teachers'

    def __str__(self):
        return f"{self.name} ({self.teacher_id})"
