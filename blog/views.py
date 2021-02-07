from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from .forms import PostForm

class BlogListView(ListView):
    model = Post
    context_object_name = "all_post_list"
    template_name = "blog/index.html"

class AboutView(TemplateView):
    template_name = "blog/about.html"

class ContactView(TemplateView):
    template_name = "blog/contact.html"


class BlogDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "blog/create.html"
    # fields = ['title', 'body']
    form_class = PostForm
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)