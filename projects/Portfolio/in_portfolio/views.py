# portfolio/views.py
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import project, Skill, Experience

class ProjectListView(ListView):
    model = project
    template_name = 'in_portfolio/project_list.html'
    context_object_name = 'projects'
    paginate_by = 9
    
    def get_queryset(self):
        project_type = self.request.GET.get('type', None)
        if project_type:
            return project.objects.filter(project_type=project_type)
        return project.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project_types'] = project.PROJECT_TYPES
        return context

class ProjectDetailView(DetailView):
    model = project
    template_name = 'in_portfolio/project_detail.html'
    context_object_name = 'project'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['technologies_list'] = self.object.get_technologies_list()
        # Get related projects
        context['related_projects'] = project.objects.filter(
            project_type=self.object.project_type
        ).exclude(id=self.object.id)[:3]
        return context