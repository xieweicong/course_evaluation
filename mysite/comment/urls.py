from django.urls import path

from . import views

app_name = "comment"

urlpatterns = [
    # 发表评论
    path("post-comment/<int:course_id>/", views.post_comment, name="post_comment"),
    path(
        "delete-comment/<int:comment_id>/", views.delete_comment, name="delete_comment"
    ),
]
