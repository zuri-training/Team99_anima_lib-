# Generated by Django 3.2 on 2022-08-03 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20220801_0832'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
