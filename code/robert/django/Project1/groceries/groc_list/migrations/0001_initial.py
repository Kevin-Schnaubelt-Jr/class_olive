# Generated by Django 4.1.1 on 2022-09-30 00:33

from pickle import TRUE
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Groceries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(null=True)),
                ('comp', models.BooleanField(default=TRUE)),
            ],
        ),
    ]
