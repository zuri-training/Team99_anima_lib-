# Generated by Django 3.2 on 2022-08-01 07:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_on']},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='created_at',
            new_name='created_on',
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=200, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Pubish')], default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
