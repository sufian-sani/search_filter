# Generated by Django 3.0.2 on 2022-02-24 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_manage', '0002_post_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Age_range',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(max_length=3)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='age_range',
            field=models.ManyToManyField(related_name='agerange', to='post_manage.Age_range'),
        ),
    ]
