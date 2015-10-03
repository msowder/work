from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'tasks/(?P<task_id>[0-9]+)/$', views.get_tasks, name='view_task'),
]