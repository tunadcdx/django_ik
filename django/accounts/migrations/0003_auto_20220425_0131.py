# Generated by Django 3.2.13 on 2022-04-24 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skils', '0001_initial'),
        ('accounts', '0002_userprofil_userfield'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofil',
            name='skils',
        ),
        migrations.AddField(
            model_name='userprofil',
            name='skils',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='skils.skils'),
        ),
    ]
