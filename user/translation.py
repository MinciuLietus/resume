from django.db.models import CharField, TextField
from modeltranslation.translator import TranslationOptions, translator

from user.models import Education, Experience, Profile, Skill, WorkStyle


def get_model_fields(model):
    return tuple(
        [
            field.attname
            for field in model._meta.fields
            if isinstance(field, TextField)
        ]
    )


class ProfileTranslationOptions(TranslationOptions):
    fields = get_model_fields(Profile)


class WorkStyleTranslationOptions(TranslationOptions):
    fields = get_model_fields(WorkStyle)


class ExperienceTranslationOptions(TranslationOptions):
    fields = get_model_fields(Experience)


class EducationTranslationOptions(TranslationOptions):
    fields = get_model_fields(Education)


class SkillTranslationOptions(TranslationOptions):
    fields = get_model_fields(Skill)


translator.register(Profile, ProfileTranslationOptions)
translator.register(WorkStyle, WorkStyleTranslationOptions)
translator.register(Experience, ExperienceTranslationOptions)
translator.register(Education, EducationTranslationOptions)
translator.register(Skill, SkillTranslationOptions)
