from django.urls import path

from . import views

urlpatterns = [
    # ex: /courses/
    # path('', views.index, name='index'),
    # ex: /courses/5/
    path('<int:course_id>/', views.detail, name='detail'),
]
