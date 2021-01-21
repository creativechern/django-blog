from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.HomepageView.as_view(), name="home"),
    path('/about', views.AboutView.as_view(), name="about"),
]