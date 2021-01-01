# Generated by Django 3.1.3 on 2020-12-26 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_pincode'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.AlterModelOptions(
            name='customuser',
            options={'ordering': ['date_joined']},
        ),
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('A', 'Admin'), ('E', 'Expert'), ('C', 'Competitor'), ('N', 'No role')], default=('N', 'No role'), max_length=300),
        ),
        migrations.AddField(
            model_name='customuser',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.event'),
        ),
    ]