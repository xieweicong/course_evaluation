from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from userprofile.models import Profile
from django.contrib.auth.models import User

from .models import Course, Comment
from .forms import CommentForm, NameForm


# def index(request):
#     course_list = Course.objects.order_by('-pub_date')[:5]
#     context = {'course_list': course_list}
#     return render(request, 'courses/index.html', context)


def detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    author = get_object_or_404(Profile, pk=(request.user.id - 1))
    form = NameForm()
    if request.method == "POST":
        commentform = CommentForm(request.POST)
        Comment.objects.create(
            course=course,
            author=author,
            comment_text=request.POST["your_comment"],
            pub_date=timezone.now(),
        )
        course = get_object_or_404(Course, pk=course_id)
        context = {"course": course, "form": form, "commentform": commentform}
        return render(request, "courses/detail.html", context)
    else:
        commentform = CommentForm()
        context = {"course": course, "form": form, "commentform": commentform}
    return render(request, "courses/detail.html", context)


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        # if form.is_valid():
        # process the data in form.cleaned_data as required
        # ...
        # redirect to a new URL:
        course_list = Course.objects.filter(course_name__icontains=request.POST["name"])
        context = {"course_list": course_list, "form": form}
        return render(request, "courses/index.html", context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
    return render(request, "courses/home.html", {"form": form})
