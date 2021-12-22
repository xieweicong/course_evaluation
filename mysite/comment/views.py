from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .forms import CommentForm
from .models import Comment
from courses.models import Course
from userprofile.models import Profile

# from notifications.signals import notify


@login_required(login_url="/userprofile/login/")
def post_comment(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    # 处理 POST 请求
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.course = course
            new_comment.user = request.user
            new_comment.save()

            # 给管理员发送通知
            # if not request.user.is_superuser:
            #     notify.send(
            #         request.user,
            #         recipient=User.objects.filter(is_superuser=1),
            #         verb="回复了你",
            #         target=course,
            #         action_object=new_comment,
            #     )

            # 添加锚点
            # redirect_url = (
            #     course.get_absolute_url() + "#comment_elem_" + str(new_comment.id)
            # )
            return redirect("courses:detail", course_id)
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    # 处理 GET 请求
    elif request.method == "GET":
        comment_form = CommentForm()
        context = {
            "comment_form": comment_form,
            "course_id": course_id,
        }
        return render(request, "comment/reply.html", context)
    # 处理其他请求
    else:
        return HttpResponse("仅接受GET/POST请求。")


@login_required(login_url="/userprofile/login/")
def delete_comment(request, comment_id):
    # 处理 POST 请求
    if request.method == "POST":
        comment = get_object_or_404(Comment, id=comment_id)
        comment.delete()
        return redirect("userprofile:user_page")
