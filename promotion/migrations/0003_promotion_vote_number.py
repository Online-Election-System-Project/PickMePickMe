# Generated by Django 4.0 on 2021-12-12 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotion', '0002_alter_promotion_candidate'),
    ]

    operations = [
        migrations.AddField(
            model_name='promotion',
            name='vote_number',
            field=models.IntegerField(default=0),
        ),
    ]