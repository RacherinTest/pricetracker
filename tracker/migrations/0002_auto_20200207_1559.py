# Generated by Django 3.0.2 on 2020-02-07 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
