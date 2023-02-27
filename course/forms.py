from django import forms
from .models import (
    Course, 
    Announcement,
    Task,
    Grade
)
from django.core.validators import (
    MinValueValidator, 
    MaxValueValidator
)


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('name', 'description', 'image',)


class CourseJoinForm(forms.Form):
    course_code = forms.IntegerField(validators=[MinValueValidator(100000), MaxValueValidator(999999)])


class AnnounceForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ('announcement', 'is_limited',)


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description', 'date_due', 'points',)


class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ('grade',)
