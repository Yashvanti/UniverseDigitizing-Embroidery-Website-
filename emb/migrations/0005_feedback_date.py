# Generated by Django 3.0.5 on 2020-08-29 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emb', '0004_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
