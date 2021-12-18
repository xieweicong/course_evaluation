from django.db import models
from userprofile.models import Profile


class Course(models.Model):
    course_name = models.CharField(max_length=200)
    teacher_name = models.CharField(max_length=200)
    class_hours = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    course_form = models.CharField(max_length=200)
    year_semester = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.course_name


class Comment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, default=1)
    comment_text = models.TextField(max_length=2000)
    pub_date = models.DateTimeField("date published")
