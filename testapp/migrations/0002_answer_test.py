# Generated by Django 4.0.3 on 2022-03-15 22:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='test',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='testapp.test'),
        ),
    ]
