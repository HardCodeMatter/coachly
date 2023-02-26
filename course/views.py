from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import (
    Course,
    Member,
    Announcement,
    Task,
    Grade
)
from .forms import (
    CourseForm, 
    CourseJoinForm,
    AnnounceForm,
    TaskForm
)
from .services import (
    course_create, 
    member_create,
    course_filter_by_user,
    announcement_create,
    task_create
)
from services import (
    all_objects,
    filter_objects, 
    get_objects
)

from random import randint


@login_required
def course_list_view(request):
    members = course_filter_by_user(request.user)

    context = {
        'members': members,
    }

    return render(request, 'course/course_list.html', context)

@login_required
def course_detail_view(request, id):
    course = get_objects(Course, id=id)
    teachers = filter_objects(Member, course=course, role='TEACHER')
    students = filter_objects(Member, course=course, role='STUDENT')
    announcements = filter_objects(Announcement, course=course).order_by('-date_created')

    if request.method == 'POST':
        form = AnnounceForm(request.POST)

        if form.is_valid():
            announcement_create(
                course=course,
                author=request.user,
                announcement=form.cleaned_data['announcement'],
                is_limited=form.cleaned_data['is_limited']
            )

            return redirect(f'/course/{course.id}/')
    else:
        form = AnnounceForm()

    context = {
        'course': course,
        'teachers': teachers,
        'students': students,
        'form': form,
        'announcements': announcements,
    }

    return render(request, 'course/course_detail.html', context)

@login_required
def course_edit_view(request, id):
    course = get_objects(Course, id=id)

    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)

        if form.is_valid():
            form.save()

            return redirect(f'/course/{course.id}/')
    else:
        form = CourseForm(instance=course)

    context = {
        'course': course,
        'form': form,
    }

    return render(request, 'course/course_edit.html', context)

@login_required
def course_create_view(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)

        if form.is_valid():
            course = course_create(
                author=request.user,
                course_code=randint(100000, 999999),
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                image=form.cleaned_data['image'],
            )
            member_create(
                user=request.user,
                course=course,
                role='TEACHER',
            )

            return redirect(f'/course/{course.pk}')
    else:
        form = CourseForm()

    context = {
        'form': form,
    }

    return render(request, 'course/course_create.html', context)

@login_required
def course_join_view(request):
    if request.method == 'POST':
        form = CourseJoinForm(request.POST)

        if form.is_valid():
            course = get_objects(Course, course_code=form.cleaned_data['course_code'])
            member = filter_objects(
                Member,
                user=request.user,
                course=course,
            )
            
            if len(member) == 0:
                member_create(
                    user=request.user,
                    course=course,
                    role='STUDENT',
                )

            return redirect(f'/course/{course.id}/')
    else:
        form = CourseJoinForm()

    context = {
        'form': form,
    }

    return render(request, 'course/course_join.html', context)


@login_required
def announcement_delete_view(request, id):
    course = get_objects(Course, announcement=id)
    teachers = filter_objects(Member, course=course, role='TEACHER')

    for teacher in teachers:
        if teacher.user == request.user:
            get_objects(Announcement, id=id).delete()
        else:
            filter_objects(Announcement, id=id, author=request.user).delete()
    
    return redirect(f'/course/{course.id}')


@login_required
def task_list_view(request, id):
    course = get_objects(Course, id=id)
    teacher = get_objects(Member, user=request.user, course=course, role='TEACHER')
    tasks = filter_objects(Task, course=course)

    context = {
        'teacher': teacher,
        'tasks': tasks,
    }

    return render(request, 'course/task_list.html', context)

@login_required
def task_detail_view(request, course_id, task_id):
    course = get_objects(Course, id=course_id)
    task = get_objects(Task, id=task_id, course=course)

    context = {
        'task': task,
    }

    return render(request, 'course/task_detail.html', context)

@login_required
def task_edit_view(request, course_id, task_id):
    course = get_objects(Course, id=course_id)
    task = get_objects(Task, id=task_id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            object = form.save(commit=False)
            object.name = form.cleaned_data['name']
            object.description = form.cleaned_data['description']
            object.date_due = form.cleaned_data['date_due']
            object.points = form.cleaned_data['points']
            
            object.save()

            return redirect(f'/course/{course.id}/task/{task.id}/')
    else:
        form = TaskForm(instance=task)

    context = {
        'course': course,
        'task': task,
        'form': form,
    }

    return render(request, 'course/task_edit.html', context)

@login_required
def task_create_view(request, id):
    course = get_objects(Course, id=id)

    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = task_create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                author=request.user,
                course=course,
                date_due=form.cleaned_data['date_due'],
                points=form.cleaned_data['points'],
            )

            return redirect(f'/course/{course.id}/task/{task.id}')
    else:
        form = TaskForm()

    context = {
        'course': course,
        'form': form,
    }

    return render(request, 'course/task_create.html', context)


@login_required
def grade_list_view(request, id):
    course = get_objects(Course, id=id)
    tasks = filter_objects(Task, course=course)
    grades = filter_objects(Grade, course=course)

    context = {
        'tasks': tasks,
        'grades': grades,
    }

    return render(request, 'course/grade_list.html', context)
