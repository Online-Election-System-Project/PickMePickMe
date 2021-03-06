# Generated by Django 3.2.9 on 2021-12-11 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.IntegerField()),
                ('party', models.CharField(max_length=100)),
                ('name_kor', models.CharField(max_length=100)),
                ('name_hanja', models.CharField(max_length=100)),
                ('sex', models.CharField(max_length=100)),
                ('birth', models.DateField(blank=True, null=True)),
                ('job', models.CharField(max_length=100)),
                ('educational_background', models.CharField(max_length=100)),
                ('career', models.CharField(max_length=100)),
                ('bulletin', models.FileField(upload_to='pdf')),
                ('poster', models.FileField(upload_to='pdf')),
                ('pledge', models.FileField(upload_to='pdf')),
            ],
        ),
    ]
