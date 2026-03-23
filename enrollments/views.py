from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Enrollment
from .forms import EnrollmentForm

@login_required
def enrollment_list(request):
    enrollments = Enrollment.objects.all().select_related('student', 'course')
    return render(request, 'enrollments/enrollment_list.html', {'enrollments': enrollments})

@login_required
def enrollment_add(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '选课成功！')
            return redirect('enrollment_list')
    else:
        form = EnrollmentForm()
    return render(request, 'enrollments/enrollment_form.html', {'form': form, 'action': '添加'})

@login_required
def enrollment_delete(request, pk):
    enrollment = get_object_or_404(Enrollment, pk=pk)
    if request.method == 'POST':
        enrollment.delete()
        messages.success(request, '退课成功！')
        return redirect('enrollment_list')
    return render(request, 'enrollments/enrollment_confirm_delete.html', {'enrollment': enrollment})
