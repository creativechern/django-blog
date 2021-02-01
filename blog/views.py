from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .models import Post
class HomepageView(TemplateView):
    template_name = "blog/index.html"


class AboutView(TemplateView):
    template_name = "blog/about.html"


class ContactView(TemplateView):
    template_name = "blog/contact.html"


class PostView(TemplateView):
    template_name = "blog/post.html"

class BlogCreateView(CreateView):
    model = Post
    template_name = "blog/create.html"
    fields = ['title', 'body']