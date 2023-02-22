from django.shortcuts import render, redirect
from .models import Course, Member
from .forms import (CourseForm, CourseJoinForm)
from .services import (
    course_create, 
    member_create,
    course_filter_by_user
)
from services import (all_objects, filter_objects, get_objects)

from random import randint


def course_list_view(request):
    members = course_filter_by_user(request.user)

    context = {
        'members': members,
    }

    return render(request, 'course/course_list.html', context)

def course_detail_view(request, id):
    course = get_objects(Course, id=id)

    context = {
        'course': course,
    }

    return render(request, 'course/course_detail.html', context)

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
        'form': form,
    }

    return render(request, 'course/course_edit.html', context)

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
