# Generated by Django 3.1.3 on 2020-12-26 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201113_0658'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='pincode',
            field=models.CharField(blank=True, max_length=4),
        ),
    ]