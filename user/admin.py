from django.contrib import admin

# Register your models here.
from user.models import Education, Experience, Profile, Skill, TechSkill, WorkStyle


admin.site.register(Profile)

admin.site.register(Skill)

admin.site.register(Education)

admin.site.register(Experience)

admin.site.register(WorkStyle)

admin.site.register(TechSkill)