# Generated by Django 3.0.8 on 2021-07-25 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_system', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='username',
        ),
        migrations.AddField(
            model_name='useraccount',
            name='first_name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='useraccount',
            name='last_name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
