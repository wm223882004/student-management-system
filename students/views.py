from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import models
from .models import Student
from .forms import StudentForm

@login_required
def student_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        students = Student.objects.filter(
            models.Q(student_id__icontains=search_query) |
            models.Q(name__icontains=search_query) |
            models.Q(major__icontains=search_query)
        )
    else:
        students = Student.objects.all()
    
    # Simple pagination
    from django.core.paginator import Paginator
    paginator = Paginator(students, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'students/student_list.html', {
        'page_obj': page_obj,
        'search_query': search_query
    })

@login_required
def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # Create User and Student together
            user = form.save_user()
            student = form.save(commit=False)
            student.user = user
            student.save()
            messages.success(request, '学生添加成功！')
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form, 'action': '添加'})

@login_required
def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, '学生信息更新成功！')
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_form.html', {'form': form, 'action': '编辑'})

@login_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.user.delete()
        student.delete()
        messages.success(request, '学生删除成功！')
        return redirect('student_list')
    return render(request, 'students/student_confirm_delete.html', {'student': student})
