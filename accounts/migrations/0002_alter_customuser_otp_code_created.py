# Generated by Django 5.0.6 on 2024-06-13 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='otp_code_created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
