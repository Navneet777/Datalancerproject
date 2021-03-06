# Generated by Django 2.2.5 on 2020-07-01 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0005_auto_20200629_1924'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrandingCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('rating', models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])),
                ('course_img', models.ImageField(upload_to='media/')),
            ],
        ),
    ]
