# Generated by Django 4.2.1 on 2023-05-22 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('date_of_birth', models.CharField(max_length=30)),
                ('date_of_visit', models.CharField(max_length=30)),
                ('name_of_doctor', models.CharField(max_length=30)),
                ('conclusion', models.CharField(max_length=30)),
            ],
        ),
    ]