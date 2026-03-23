from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Teacher
from .forms import TeacherForm

@login_required
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers/teacher_list.html', {'teachers': teachers})

@login_required
def teacher_add(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            user = form.save_user()
            teacher = form.save(commit=False)
            teacher.user = user
            teacher.save()
            messages.success(request, '教师添加成功！')
            return redirect('teacher_list')
    else:
        form = TeacherForm()
    return render(request, 'teachers/teacher_form.html', {'form': form, 'action': '添加'})

@login_required
def teacher_edit(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            messages.success(request, '教师信息更新成功！')
            return redirect('teacher_list')
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'teachers/teacher_form.html', {'form': form, 'action': '编辑'})

@login_required
def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        teacher.user.delete()
        teacher.delete()
        messages.success(request, '教师删除成功！')
        return redirect('teacher_list')
    return render(request, 'teachers/teacher_confirm_delete.html', {'teacher': teacher})
