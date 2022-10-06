# Generated by Django 3.2.15 on 2022-09-16 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('family_member', '0003_alter_familymember_family_member_img'),
        ('task', '0002_task_belongs_to_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='assigned',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_family_member', to='family_member.familymember'),
        ),
    ]