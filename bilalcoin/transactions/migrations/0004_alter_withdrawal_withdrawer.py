# Generated by Django 3.2.3 on 2021-08-03 04:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('transactions', '0003_auto_20210803_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='withdrawal',
            name='withdrawer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='withdrawals', to=settings.AUTH_USER_MODEL),
        ),
    ]