from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'欢迎回来，{user.username}！')
            return redirect('dashboard')
        else:
            messages.error(request, '用户名或密码错误')
    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    messages.info(request, '您已成功退出登录')
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'注册成功，欢迎 {user.username}！')
            return redirect('dashboard')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def dashboard(request):
    from students.models import Student
    from courses.models import Course
    from grades.models import Grade
    
    student_count = Student.objects.count()
    course_count = Course.objects.count()
    grade_count = Grade.objects.count()
    
    avg_score = None
    if grade_count > 0:
        from django.db.models import Avg
        avg_score = Grade.objects.aggregate(Avg('score'))['score__avg']
        avg_score = round(avg_score, 2) if avg_score else 0
    
    context = {
        'student_count': student_count,
        'course_count': course_count,
        'grade_count': grade_count,
        'avg_score': avg_score,
    }
    return render(request, 'users/dashboard.html', context)
