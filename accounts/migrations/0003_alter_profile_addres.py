# Generated by Django 4.0.4 on 2022-05-19 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile_addres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='addres',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]