# Generated by Django 3.2.16 on 2022-12-25 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mfadmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('accountNo', models.BigIntegerField(default=0, unique=True)),
                ('user', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='mfadmin.user')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_key',
            field=models.CharField(default='1ac85e8b5e', max_length=10, unique=True),
        ),
    ]