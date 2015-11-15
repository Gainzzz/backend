from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'all/$', views.all_muscles, name='all_muscles'),
    url(r'(?P<muscle_id>[0-9]+)/$', views.muscle, name='muscle'),
    url(r'(?P<name>[A-Za-z]+)/$', views.muscle_name, name='muscle_name'),
]