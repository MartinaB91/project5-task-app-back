# Generated by Django 3.2.15 on 2022-10-07 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('family_member', '0004_alter_familymember_family_member_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familymember',
            name='family_member_img',
            field=models.ImageField(blank=True, default='../rabbit-face-svgrepo-com_frcjxf', upload_to='images/'),
        ),
    ]
