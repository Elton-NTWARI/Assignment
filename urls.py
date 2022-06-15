from importlib.resources import path
from blog import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('detail.html', views.detail, name='detail'),
]