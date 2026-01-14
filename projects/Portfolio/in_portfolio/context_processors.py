# in_portfolio/context_processors.py
from .models import project, Skill

def project_context(request):
    """
    Makes Project and Skill data available in all templates.
    """
    return {
        "all_projects": project.objects.all(),
        "all_skills": Skill.objects.all(),
    }
