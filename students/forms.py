from django import forms
from django.contrib.auth.models import User
from .models import Student

class StudentForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True, label='用户名')
    password = forms.CharField(widget=forms.PasswordInput, required=True, label='密码')
    student_id = forms.CharField(max_length=20, required=True, label='学号')
    name = forms.CharField(max_length=50, required=True, label='姓名')
    gender = forms.ChoiceField(choices=Student.GENDER_CHOICES, widget=forms.RadioSelect, label='性别')
    age = forms.IntegerField(required=True, label='年龄')
    major = forms.CharField(max_length=100, required=True, label='专业')
    enrollment_year = forms.IntegerField(required=True, label='入学年份')
    phone = forms.CharField(max_length=11, required=False, label='电话')
    email = forms.EmailField(required=False, label='邮箱')
    address = forms.CharField(widget=forms.Textarea, required=False, label='地址')

    class Meta:
        model = Student
        fields = ['student_id', 'name', 'gender', 'age', 'major', 'enrollment_year', 'phone', 'email', 'address']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if not isinstance(field.widget, (forms.RadioSelect, forms.Textarea, forms.PasswordInput)):
                field.widget.attrs.update({'class': 'form-control'})

    def save_user(self):
        from users.models import User as CustomUser
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        email = self.cleaned_data.get('email', '')
        
        user = CustomUser.objects.create_user(
            username=username,
            password=password,
            email=email
        )
        user.role = 'student'
        user.save()
        return user

    def save(self, commit=True):
        student = super().save(commit=False)
        if commit:
            student.save()
        return student
