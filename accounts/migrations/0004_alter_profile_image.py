# Generated by Django 4.0.4 on 2022-05-20 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_profile_addres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='defualt.png', upload_to='profiles_img/%y/%m/%d'),
        ),
    ]