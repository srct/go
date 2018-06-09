# Generated by Django 2.0.5 on 2018-06-08 20:58

from django.db import migrations, models
import django.utils.timezone
import go.validators


class Migration(migrations.Migration):

    dependencies = [
        ('go', '0003_auto_20180524_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Go Link Creation Date'),
        ),
        migrations.AlterField(
            model_name='url',
            name='destination',
            field=models.URLField(default='https://go.gmu.edu', help_text='The URL to be redirected to when visiting the shortlink.', max_length=1000),
        ),
        migrations.AlterField(
            model_name='url',
            name='owner',
            field=models.ForeignKey(on_delete='cascade', to='go.RegisteredUser', verbose_name='RegisteredUser Owner'),
        ),
        migrations.AlterField(
            model_name='url',
            name='short',
            field=models.CharField(help_text='The shortcode that acts as the unique go link.', max_length=20, unique=True, validators=[go.validators.unique_short_validator, go.validators.regex_short_validator]),
        ),
    ]
