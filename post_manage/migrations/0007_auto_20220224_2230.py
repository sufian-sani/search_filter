# Generated by Django 3.0.2 on 2022-02-24 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_manage', '0006_auto_20220224_1903'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='age_range',
        ),
        migrations.AddField(
            model_name='post',
            name='salary',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
