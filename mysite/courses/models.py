from django.db import models
from userprofile.models import Profile

from django.urls import reverse


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

    # 获取文章地址
    def get_absolute_url(self):
        return reverse("course:detail", args=[self.id])
