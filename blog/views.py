from django.shortcuts import render
from django.views.generic import TemplateView

class HomepageView(TemplateView):
    template_name = "blog/index.html"


class AboutView(TemplateView):
    template_name = "blog/about.html"
