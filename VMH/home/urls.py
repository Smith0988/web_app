from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_home, name="home"),
    path('search/', views.search, name='search'),
]
