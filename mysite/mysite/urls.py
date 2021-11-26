from django.contrib import admin
from django.urls import include, path

from courses import views


urlpatterns = [
    path('', views.get_name, name='get_name'),
    path('courses/', include('courses.urls')),
    path('admin/', admin.site.urls),
]
