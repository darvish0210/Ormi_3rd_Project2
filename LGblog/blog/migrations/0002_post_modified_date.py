# Generated by Django 4.2.7 on 2023-11-06 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]