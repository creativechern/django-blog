from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Post
from .forms import PostForm

class BlogListView(ListView):
    model = Post
    template_name = "blog/index.html"

class AboutView(TemplateView):
    template_name = "blog/about.html"

class ContactView(TemplateView):
    template_name = "blog/contact.html"


class BlogDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

class BlogCreateView(CreateView):
    model = Post
    template_name = "blog/create.html"
    # fields = ['title', 'body']
    form_class = PostForm