# Generated by Django 3.0.3 on 2020-02-06 01:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('useradm', '0002_auto_20200205_2352'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ctclient',
            options={'ordering': ['first_name', 'last_name', 'iban'], 'verbose_name_plural': 'Clients'},
        ),
    ]
