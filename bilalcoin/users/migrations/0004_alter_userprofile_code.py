# Generated by Django 3.2.3 on 2021-05-31 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_userprofile_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='code',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
    ]
