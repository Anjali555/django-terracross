from django.conf.urls import url
from polls import views

urlpatterns = [
    url('', views.index, name='index'),
]