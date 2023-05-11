# Generated by Django 4.1.5 on 2023-05-04 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=200, verbose_name='Имя студента')),
                ('student_course', models.IntegerField(verbose_name='Курс')),
                ('student_group', models.IntegerField(verbose_name='Группа')),
                ('student_general_works', models.IntegerField(verbose_name='Общее число работ')),
                ('student_done_works', models.IntegerField(verbose_name='Количество выполненных работ')),
                ('student_programming_lang', models.CharField(max_length=20, verbose_name='Язык программирования')),
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'Студенты',
            },
        ),
    ]
