from django import forms
from users.models import User
from .models import Teacher

class TeacherForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True, label='用户名')
    password = forms.CharField(widget=forms.PasswordInput, required=True, label='密码')
    teacher_id = forms.CharField(max_length=20, required=True, label='教师编号')
    name = forms.CharField(max_length=50, required=True, label='姓名')
    title = forms.CharField(max_length=50, required=False, label='职称')
    department = forms.CharField(max_length=100, required=True, label='所属院系')
    phone = forms.CharField(max_length=11, required=False, label='电话')
    email = forms.EmailField(required=False, label='邮箱')

    class Meta:
        model = Teacher
        fields = ['teacher_id', 'name', 'title', 'department', 'phone', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if not isinstance(field.widget, forms.PasswordInput):
                field.widget.attrs.update({'class': 'form-control'})

    def save_user(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        email = self.cleaned_data.get('email', '')
        
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email
        )
        user.role = 'teacher'
        user.save()
        return user

    def save(self, commit=True):
        teacher = super().save(commit=False)
        if commit:
            teacher.save()
        return teacher
