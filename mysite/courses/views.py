from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from userprofile.models import Profile
from comment.models import Comment
from django.contrib.auth.models import User

from .models import Course
from .forms import SearchForm


# def index(request):
#     course_list = Course.objects.order_by('-pub_date')[:5]
#     context = {'course_list': course_list}
#     return render(request, 'courses/index.html', context)


def detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    # author = get_object_or_404(Profile, pk=(request.user.id - 1))
    comments = Comment.objects.filter(course=course_id)
    form = SearchForm()
    context = {"course": course, "form": form, "comments": comments}
    return render(request, "courses/detail.html", context)


def search_course(request):
    if request.method == "POST":
        search_form = SearchForm(data=request.POST)
        if search_form.is_valid():
            data = search_form.cleaned_data
            course_list = Course.objects.filter(course_name__icontains=data["searchCourse"])
            context = {"course_list": course_list}
            return render(request, "courses/index.html", context)
    # if a GET (or any other method) we'll create a blank form
    else:
        search_form = SearchForm()
        course_list = Course.objects.order_by('?')[:12]
    return render(request, "courses/home.html", {"form": search_form, "course_list": course_list})
