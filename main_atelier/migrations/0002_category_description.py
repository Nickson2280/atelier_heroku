# Generated by Django 3.2 on 2021-04-22 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_atelier', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.CharField(max_length=400, null=True),
        ),
    ]