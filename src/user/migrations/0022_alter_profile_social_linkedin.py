# Generated by Django 3.2.5 on 2021-08-29 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0021_rename_bio_second_profile_bio_tab'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='social_linkedin',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]