# Generated by Django 4.2.5 on 2023-09-30 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school_class_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolClassStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('roll_number', models.IntegerField()),
                ('mobile', models.CharField(max_length=10)),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_class_api.schoolclass')),
            ],
        ),
    ]
