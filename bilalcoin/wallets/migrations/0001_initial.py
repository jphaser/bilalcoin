# Generated by Django 3.1.10 on 2021-05-13 19:48

from django.db import migrations, models
import django.utils.timezone
import bilalcoin.wallets.models
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('owner', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='Wallet Owner')),
                ('walletID', models.CharField(blank=True, max_length=36, null=True, unique=True, verbose_name='Wallet ID')),
                ('qrcode', models.ImageField(null=True, upload_to=bilalcoin.wallets.models.qrcode_image_path, verbose_name='QR Code')),
                ('active', models.BooleanField(default=False, verbose_name='Wallet is Active?')),
            ],
            options={
                'verbose_name': 'Wallet',
                'verbose_name_plural': 'Wallets',
                'ordering': ['created'],
            },
        ),
    ]
