from django.db import models
from django.contrib.auth.models import User, update_last_login
import uuid
from django.db.models.base import ModelState
from django.db.models.fields import TextField

from django.db.models.fields.related import ManyToManyField

# Create your models here.


class Skill(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)


class Education(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    created_from = models.CharField(max_length=100, blank=True, null=True)
    created_to = models.CharField(max_length=100, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)


class Experience(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    company = models.TextField(blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    created_from = models.CharField(max_length=100, blank=True, null=True)
    created_to = models.CharField(max_length=100, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)


class WorkStyle(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    about = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.name)


class TechSkill(models.Model):
    programming_languages = models.JSONField(default=list, null=True, blank=True)
    frameworks = models.JSONField(default=list, null=True, blank=True)
    developer_tools = models.JSONField(default=list, null=True, blank=True)
    libraries = models.JSONField(default=list, null=True, blank=True)
    other = models.JSONField(default=list, null=True, blank=True)


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    skills = models.ForeignKey(TechSkill, on_delete=models.DO_NOTHING, null=True, blank=True)
    
    languages = models.ManyToManyField(Skill, related_name='languages', blank=True)
    education = models.ManyToManyField(Education, related_name='education', blank=True)
    experience = models.ManyToManyField(Experience, related_name='education', blank=True)
    workstyle = models.ManyToManyField(WorkStyle, related_name='workstyle', blank=True)

    name = models.CharField(max_length=200, blank=True, null=True)
    surname = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    short_intro = models.TextField(blank=True, null=True)
    intro = models.TextField(blank=True, null=True)
    intro_tab = models.TextField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    bio_tab = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/', default='profiles/user-default.png')
    cv_file = models.FileField(null=True, blank=True, upload_to='profiles/')
    mobile_number = models.CharField(max_length=200, blank=True, null=True)
    social_github = models.CharField(max_length=200, blank=True, null=True)
    social_twitter = models.CharField(max_length=200, blank=True, null=True)
    social_linkedin = models.CharField(max_length=200, blank=True, null=True)
    social_youtube = models.CharField(max_length=200, blank=True, null=True)
    social_website = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)
