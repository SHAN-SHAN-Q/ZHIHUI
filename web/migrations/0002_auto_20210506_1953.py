# Generated by Django 3.2 on 2021-05-06 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [

        migrations.AlterField(
            model_name='eachclass',
            name='Earnestpeopl',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
    ]