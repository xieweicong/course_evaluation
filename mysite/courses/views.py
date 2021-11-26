from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Course
from .forms import NameForm


# def index(request):
#     course_list = Course.objects.order_by('-pub_date')[:5]
#     context = {'course_list': course_list}
#     return render(request, 'courses/index.html', context)


def detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    form = NameForm()
    return render(request, 'courses/detail.html', {'course': course, 'form': form})


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        # if form.is_valid():
        # process the data in form.cleaned_data as required
        # ...
        # redirect to a new URL:
        course_list = Course.objects.filter(
            course_name__icontains=request.POST['name'])
        context = {'course_list': course_list, 'form': form}
        return render(request, 'courses/index.html', context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
    return render(request, 'courses/home.html', {'form': form})
