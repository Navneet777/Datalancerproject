# Generated by Django 2.2.5 on 2020-06-29 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0004_auto_20200629_0104'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=200)),
                ('roll_no', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(default='', max_length=500)),
                ('english_marks', models.IntegerField(default=0)),
                ('math_marks', models.IntegerField(default=0)),
                ('science_marks', models.IntegerField(default=0)),
                ('name', models.ForeignKey(on_delete='do_nothing', to='info.BasicInfo')),
            ],
        ),
        migrations.DeleteModel(
            name='Edata',
        ),
    ]
