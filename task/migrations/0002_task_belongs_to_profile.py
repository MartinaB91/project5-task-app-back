# Generated by Django 3.2.15 on 2022-09-16 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='belongs_to_profile',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='profiles.profile'),
        ),
    ]
