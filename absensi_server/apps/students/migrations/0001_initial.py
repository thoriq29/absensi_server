# Generated by Django 2.1.7 on 2019-02-16 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('NIS', models.CharField(max_length=50)),
                ('academic_field', models.PositiveSmallIntegerField(choices=[(1, 'Rekayasa Perangkat Lunak'), (2, 'Teknik Komputer Jaringan'), (3, 'Akuntansi'), (4, 'Administrasi Perkantoran'), (5, 'Tata Niaga')])),
                ('grade', models.PositiveSmallIntegerField(choices=[(1, 'X'), (2, 'XI'), (3, 'XII')])),
                ('gender', models.PositiveSmallIntegerField(choices=[(1, 'Male'), (2, 'Female')])),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
            ],
        ),
    ]
