# Generated by Django 4.0.4 on 2022-05-19 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='addres',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]