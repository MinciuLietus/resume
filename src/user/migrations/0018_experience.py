# Generated by Django 3.2.5 on 2021-08-29 10:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_profile_intro_tab'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('about', models.TextField(blank=True, null=True)),
                ('created_from', models.CharField(blank=True, max_length=100, null=True)),
                ('created_to', models.CharField(blank=True, max_length=100, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
