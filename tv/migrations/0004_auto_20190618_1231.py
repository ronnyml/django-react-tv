# Generated by Django 2.2.2 on 2019-06-18 17:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv', '0003_auto_20190618_1226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='awardcategory',
            name='first_awarded_year',
        ),
        migrations.AddField(
            model_name='awardcategory',
            name='creation_year',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movietvshow',
            name='no_seasons',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)]),
        ),
    ]
