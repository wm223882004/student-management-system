from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Max, Min
from .models import Grade
from .forms import GradeForm

@login_required
def grade_list(request):
    grades = Grade.objects.all().select_related('student', 'course')
    return render(request, 'grades/grade_list.html', {'grades': grades})

@login_required
def grade_add(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '成绩添加成功！')
            return redirect('grade_list')
    else:
        form = GradeForm()
    return render(request, 'grades/grade_form.html', {'form': form, 'action': '添加'})

@login_required
def grade_edit(request, pk):
    grade = get_object_or_404(Grade, pk=pk)
    if request.method == 'POST':
        form = GradeForm(request.POST, instance=grade)
        if form.is_valid():
            form.save()
            messages.success(request, '成绩更新成功！')
            return redirect('grade_list')
    else:
        form = GradeForm(instance=grade)
    return render(request, 'grades/grade_form.html', {'form': form, 'action': '编辑'})

@login_required
def grade_delete(request, pk):
    grade = get_object_or_404(Grade, pk=pk)
    if request.method == 'POST':
        grade.delete()
        messages.success(request, '成绩删除成功！')
        return redirect('grade_list')
    return render(request, 'grades/grade_confirm_delete.html', {'grade': grade})

@login_required
def grade_statistics(request):
    from courses.models import Course
    from students.models import Student
    
    # Overall stats
    stats = Grade.objects.aggregate(
        avg_score=Avg('score'),
        max_score=Max('score'),
        min_score=Min('score')
    )
    
    # Stats by course
    course_stats = []
    for course in Course.objects.all():
        course_grades = Grade.objects.filter(course=course)
        if course_grades.exists():
            cs = course_grades.aggregate(avg=Avg('score'), max=Max('score'), min=Min('score'))
            course_stats.append({
                'course': course,
                'count': course_grades.count(),
                'avg': round(cs['avg'], 2) if cs['avg'] else 0,
                'max': cs['max'],
                'min': cs['min'],
            })
    
    # Failing grades
    failing_grades = Grade.objects.filter(score__lt=60).select_related('student', 'course')
    
    context = {
        'stats': stats,
        'course_stats': course_stats,
        'failing_grades': failing_grades,
    }
    return render(request, 'grades/grade_statistics.html', context)
