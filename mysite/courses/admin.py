from django.contrib import admin

from .models import Course
from comment.models import Comment


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 3


class CourseAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     (None,               {'fields': ['course_name']}),
    #     ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    # ]
    search_fields = ["course_name"]
    inlines = [CommentInline]


admin.site.register(Course, CourseAdmin)
