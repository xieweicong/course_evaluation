from django.db import models

from userprofile.models import Profile
from courses.models import Course
from django.contrib.auth.models import User


# 博文的评论
class Comment(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    body = models.TextField(max_length=2000)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('pub_date',)

    def __str__(self):
        return self.body[:20]
