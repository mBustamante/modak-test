# Generated by Django 4.2 on 2023-06-18 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0003_alter_notificationtype_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='data',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
