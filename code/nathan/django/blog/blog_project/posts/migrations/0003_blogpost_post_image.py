# Generated by Django 4.1.2 on 2022-10-14 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_blogpost_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='post_image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
