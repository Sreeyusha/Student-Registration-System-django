# Generated by Django 4.2.3 on 2023-08-06 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=30)),
                ('s_father_name', models.CharField(max_length=30)),
                ('s_contact_no', models.CharField(max_length=30)),
                ('s_parent_c_no', models.CharField(max_length=30)),
                ('s_course_id', models.CharField(max_length=30)),
                ('s_program_id', models.CharField(max_length=30)),
                ('s_addr', models.CharField(max_length=30)),
                ('s_batch', models.CharField(max_length=30)),
                ('s_email', models.CharField(max_length=30)),
                ('s_date', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='stud',
        ),
    ]
