# pages/views.py
from django.shortcuts import render
from django.views.generic import TemplateView
from in_portfolio.models import project, Skill, Experience
from blog.models import Post

class HomeView(TemplateView):
    template_name = 'pages/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_projects'] = project.objects.filter(featured=True)[:3]
        context['recent_posts'] = Post.objects.filter(is_published=True)[:3]
        context['skills'] = Skill.objects.all()
        context['experiences'] = Experience.objects.all()
        return context

class AboutView(TemplateView):
    template_name = 'pages/about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['skills'] = Skill.objects.all()
        context['experiences'] = Experience.objects.all()
        return context