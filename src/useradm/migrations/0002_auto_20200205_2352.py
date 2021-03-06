# Generated by Django 3.0.3 on 2020-02-05 23:52

from django.db import migrations, models
import useradm.validators


class Migration(migrations.Migration):

    dependencies = [
        ('useradm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ctclient',
            name='iban',
            field=models.CharField(help_text='Client IBAN account', max_length=50, unique=True, validators=[useradm.validators.IbanValidator]),
        ),
    ]
