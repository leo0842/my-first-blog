# Generated by Django 3.0.7 on 2020-07-20 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sungsani', '0002_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='revised_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]