# Generated by Django 2.0.3 on 2019-02-21 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0011_episode_tagline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='name',
            field=models.CharField(blank=True, choices=[('Y', 'YES'), ('N', 'NO')], default=None, max_length=255, null=True),
        ),
    ]