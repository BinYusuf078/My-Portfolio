# portfolio/admin.py
from django.contrib import admin
from .models import project, Skill, Experience

@admin.register(project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'project_type', 'featured', 'created_date')
    list_filter = ('project_type', 'featured', 'created_date')
    search_fields = ('title', 'description', 'technologies')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('featured',)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'category', 'order')
    list_filter = ('level', 'category')
    search_fields = ('name', 'category')

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company', 'start_date', 'end_date', 'currently_working')
    list_filter = ('company', 'currently_working')
    search_fields = ('job_title', 'company', 'description')