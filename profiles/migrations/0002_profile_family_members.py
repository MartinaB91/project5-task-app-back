# Generated by Django 3.2.15 on 2022-08-28 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('family_member', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='family_members',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='family_member.familymember'),
        ),
    ]
