# Generated by Django 5.0.6 on 2024-05-30 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(max_length=2),
        ),
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='user',
            name='state',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='user',
            name='zipcode',
            field=models.IntegerField(max_length=5),
        ),
    ]
