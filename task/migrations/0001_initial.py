# Generated by Django 3.2.15 on 2022-10-16 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('family_member', '0001_initial'),
        ('profiles', '0001_initial'),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('description', models.TextField()),
                ('star_points', models.IntegerField(default='0')),
                ('status', models.CharField(choices=[('Todo', 'Todo'), ('Done', 'Done')], default='Todo', max_length=6)),
                ('assigned', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_family_member', to='family_member.familymember')),
                ('belongs_to_profile', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='task_category', to='categories.category')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_creator', to='family_member.familymember')),
            ],
        ),
    ]
