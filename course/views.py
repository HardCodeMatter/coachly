from django.shortcuts import render, redirect
from .models import Course
from .forms import CourseForm
from .services import course_create
from services import all_objects

from random import randint


def course_list_view(request):
    courses = all_objects(Course)

    context = {
        'courses': courses,
    }

    return render(request, 'course/course_list.html', context)

def course_create_view(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)

        if form.is_valid():
            course_create(
                author=request.user,
                course_code=randint(100000, 999999),
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                image=form.cleaned_data['image'],
            )

            return redirect('/course/')
    else:
        form = CourseForm()

    context = {
        'form': form,
    }

    return render(request, 'course/course_create.html', context)