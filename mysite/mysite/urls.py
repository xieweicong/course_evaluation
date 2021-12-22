from django.contrib import admin
from django.urls import include, path

from courses import views


urlpatterns = [
    path("", views.search_course, name="search_course"),
    path("courses/", include("courses.urls", namespace="courses")),
    path("admin/", admin.site.urls),
    path("user/", include("userprofile.urls")),
    path("comment/", include("comment.urls", namespace="comment")),
]
