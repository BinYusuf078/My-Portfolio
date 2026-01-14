# portfolio/models.py
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class project(models.Model):
    PROJECT_TYPES = [
        ('web', 'Web Development'),
        ('mobile', 'Mobile App'),
        ('data', 'Data Science'),
        ('other', 'Other'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    project_type = models.CharField(max_length=20, choices=PROJECT_TYPES, default='web')
    featured_image = models.ImageField(upload_to='project_images/')
    github_url = models.URLField(blank=True)
    live_demo_url = models.URLField(blank=True)
    technologies = models.CharField(max_length=300, help_text="Comma-separated list of technologies")
    featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('in_portfolio:project_detail', kwargs={'slug': self.slug})
    
    def get_technologies_list(self):
        return [tech.strip() for tech in self.technologies.split(',')]

class Skill(models.Model):
    SKILL_LEVELS = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('expert', 'Expert'),
    ]
    
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=20, choices=SKILL_LEVELS, default='intermediate')
    category = models.CharField(max_length=100, blank=True)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['category', 'order']
    
    def __str__(self):
        return f"{self.name} ({self.get_level_display()})"

class Experience(models.Model):
    job_title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=100, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    currently_working = models.BooleanField(default=False)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['-start_date']
    
    def __str__(self):
        return f"{self.job_title} at {self.company}"