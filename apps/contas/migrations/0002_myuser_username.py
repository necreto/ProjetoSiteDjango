# Generated by Django 5.1.2 on 2024-11-03 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='username',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]
