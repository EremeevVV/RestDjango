# Generated by Django 3.1.3 on 2020-11-13 06:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(max_length=30, verbose_name="user's first name")),
                ('last_name', models.CharField(max_length=30, verbose_name="user's last name")),
                ('photo', models.ImageField(blank=True, height_field=300, null=True, upload_to='user_photos', width_field=200)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('country', models.CharField(choices=[('US', 'United States'), ('FR', 'France'), ('CN', 'China'), ('RU', 'Russia'), ('IT', 'Italy')], max_length=300)),
                ('about', models.TextField(blank=True, max_length=300, null=True, verbose_name='about')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
