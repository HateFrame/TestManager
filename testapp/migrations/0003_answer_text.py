# Generated by Django 4.0.3 on 2022-03-17 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_answer_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='text',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
