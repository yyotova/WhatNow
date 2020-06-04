# Generated by Django 3.0.6 on 2020-06-03 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200603_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='current_locations',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='interests',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='skills',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='technologies',
            field=models.TextField(null=True),
        ),
    ]
