# Generated by Django 2.2.2 on 2019-06-18 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv', '0004_auto_20190618_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movietvshow',
            name='running_time',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]