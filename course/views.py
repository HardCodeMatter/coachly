from django.shortcuts import render, redirect
from .models import Course
from .forms import CourseForm

from random import randint


def course_list(request):
    courses = Course.objects.all()

    context = {
        'courses': courses,
    }

    return render(request, 'course/course_list.html', context)

def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)

        if form.is_valid():
            object = form.save(commit=False)
            object.author = request.user
            object.course_code = randint(100000, 999999)
            object.save()

            return redirect('/course')
    else:
        form = CourseForm()

    context = {
        'form': form,
    }

    return render(request, 'course/course_create.html', context)
