# Generated by Django 4.2.6 on 2023-10-05 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudyCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Учебного Центра',
                'verbose_name_plural': 'Учебные Центры',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=256)),
                ('about', models.CharField(blank=True, max_length=256, null=True)),
                ('experience', models.PositiveIntegerField(blank=True, max_length=256, null=True)),
                ('phone_number', models.CharField(max_length=256)),
                ('study_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.studycenter')),
            ],
            options={
                'verbose_name': 'Учителья',
                'verbose_name_plural': 'Учители',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=256)),
                ('about', models.CharField(blank=True, max_length=256, null=True)),
                ('phone_number', models.CharField(max_length=256)),
                ('study_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.studycenter')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.teacher')),
            ],
            options={
                'verbose_name': 'Студента',
                'verbose_name_plural': 'Студенты',
            },
        ),
    ]
