# Generated by Django 4.2 on 2023-05-17 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pythonapp', '0003_delete_individuals'),
    ]

    operations = [
        migrations.CreateModel(
            name='individuals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('images', models.ImageField(upload_to='pictures')),
                ('descr', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='places',
        ),
    ]
