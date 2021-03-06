# Generated by Django 3.2 on 2021-04-22 19:35

from django.db import migrations, models
import django.db.models.deletion
import main_atelier.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_atelier', '0002_category_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('is_visible', models.BooleanField(default=True)),
                ('description', models.CharField(max_length=400, null=True)),
                ('photo', models.ImageField(upload_to=main_atelier.models.Service.get_file_name_service)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_atelier.category')),
            ],
        ),
    ]
