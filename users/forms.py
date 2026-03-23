from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=False)
    role = forms.ChoiceField(choices=User.ROLE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=11, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '手机号'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'role', 'phone')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '用户名'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': '邮箱'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name not in ['role', 'phone']:
                field.widget.attrs.update({'class': 'form-control', 'placeholder': field.label})
