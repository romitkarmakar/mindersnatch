# Generated by Django 2.1.4 on 2020-03-31 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mindapp', '0017_auto_20200331_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='message',
            field=models.CharField(default='na', max_length=200),
        ),
    ]
