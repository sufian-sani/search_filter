# Generated by Django 3.0.2 on 2022-02-24 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_manage', '0003_auto_20220224_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='age_range',
            name='age',
            field=models.IntegerField(max_length=10),
        ),
    ]