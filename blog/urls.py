from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.HomepageView.as_view(), name="home"),
    path('about/', views.AboutView.as_view(), name="about"),
    path('contact/', views.ContactView.as_view(), name="contact"),
    path('post/', views.PostView.as_view(), name="post"),
    path('post/new/', views.BlogCreateView.as_view(), name="post_new"),
]