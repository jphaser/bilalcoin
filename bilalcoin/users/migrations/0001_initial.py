# Generated by Django 3.2.3 on 2021-05-21 04:17

import bilalcoin.users.models
import bilalcoin.utils.validators
import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('countries_plus', '0005_auto_20160224_1804'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('middle_name', models.CharField(blank=True, help_text='Not compulsary, But good practive to differentciate owners', max_length=255, null=True, verbose_name='Middle Name')),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=20, null=True, verbose_name='Current Balance')),
                ('unique_id', models.UUIDField(default=uuid.uuid1, editable=False)),
                ('member_since', models.DateField(default=datetime.datetime.now)),
                ('is_verified', models.BooleanField(default=False)),
                ('has_deposited', models.BooleanField(default=False)),
                ('deposit_date', models.DateField(blank=True, default=datetime.datetime.now, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=500, null=True, verbose_name="Testimonial Giver's Name")),
                ('desc', models.TextField(max_length=1200, null=True, verbose_name='Testimonial description')),
                ('pic', models.ImageField(help_text='Must be Image files', null=True, upload_to=bilalcoin.users.models.testimonial_image, verbose_name='Testimonial Sender Image')),
            ],
            options={
                'verbose_name': 'Testimonial',
                'verbose_name_plural': 'Testimonials',
                'ordering': ['-modified'],
            },
        ),
        migrations.CreateModel(
            name='UserVerify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id_type', models.CharField(blank=True, choices=[('PASSPORT', 'PASSPORT'), ('ID_CARD', 'ID CARD'), ('DRIVERS_LICENSE', 'DRIVERS LICENSE')], default='PASSPORT', max_length=15, null=True)),
                ('id_front', models.FileField(help_text='Must be SVG, PNG or JPG files', null=True, upload_to=bilalcoin.users.models.idcard_image, validators=[bilalcoin.utils.validators.validate_uploaded_image_extension], verbose_name='ID Card Front')),
                ('id_back', models.FileField(help_text='Must be SVG, PNG or JPG files', null=True, upload_to=bilalcoin.users.models.idcard_image, validators=[bilalcoin.utils.validators.validate_uploaded_image_extension], verbose_name='ID Card Back')),
                ('ssn', models.CharField(blank=True, help_text='Must be valid Social Security Number. *** US Citizens Only', max_length=16, null=True, unique=True, validators=[django.core.validators.RegexValidator(code='Invalid_input, Only Integers', message='Must Contain Numbers Only', regex='^[0-9]*$')], verbose_name='US SSN')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userverify', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Verify',
                'verbose_name_plural': 'User Verifies',
                'ordering': ['-modified'],
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('passport', models.FileField(null=True, upload_to=bilalcoin.users.models.profile_image, validators=[bilalcoin.utils.validators.validate_uploaded_image_extension], verbose_name='User Profile Passport')),
                ('bank', models.CharField(blank=True, choices=[('', 'Select Bank'), ('Arvest Bank', 'Arvest Bank'), ('Ally Financial', 'Ally Financial'), ('American Express', 'American Express'), ('Amarillos National Bank', 'Amarillos National Bank'), ('Apple bank for Savings', 'Apple bank for Savings'), ('Bank of Hawaii', 'Bank of Hawaii'), ('Bank of Hope', 'Bank of Hope'), ('Bank United', 'Bank United'), ('BOA', 'Bank of America'), ('Bank United', 'Bank United'), ('Brown Brothers Harriman & Co', 'Brown Brothers Harriman & Co'), ('Barclays', 'Barclays'), ('BMO Harris Bank', 'BMO Harris Bank'), ('Bank OZK', 'Bank OZK'), ('BBVA Compass', 'BBVA Compass'), ('BNP Paribas', 'BNP Paribas'), ('BOK Financial Corporation', 'BOK Financial Corporation'), ('Cathay Bank', 'Cathay Bank'), ('Chartway Federal Credit Union', 'Chartway Federal Credit Union'), ('Capital One', 'Capital One'), ('Capital City Bank', 'Capital City Bank'), ('Chase Bank', 'Chase Bank'), ('Charles Schwab Corporation', 'Charles Schwab Corporation'), ('CG', 'CitiGroup'), ('Credit Suisse', 'Credit Suisse'), ('Comerica', 'Comerica'), ('CIT Group', 'CIT Group'), ('CapitalCity Bank', 'CapitalCity Bank'), ('Credit Union Page', 'Credit Union Page'), ('Citizens Federal Bank', 'Citizens Federal Bank'), ('Chemical Financial Corporation', 'Chemical Financial Corporation'), ('Discover Financial', 'Discover Finacial'), ('Deutsche Bank', 'Deutsche Bank'), ('Douglas County Bank & Trust', 'Douglas County Bank & Trust '), ('Dime Savings Bank of Williamsburgh', 'Dime Savings Bank of Williamsburgh'), ('East West Bank', 'East West Bank'), ('Flagster Bank', 'Flagster Bank'), ('First National of Nebraska', 'First National of Nebraska'), ('FirstBank Holding Co', 'FirstBank Holding Co'), ('First Capital Bank', 'First Capital Bank'), ('First Commercial Bank', 'First Commercial Bank'), ('First Federal Savings Bank of Indiana', 'First Federal Savings Bank of Indiana'), ('First Guaranty Bank of Florida', 'First Guaranty Bank of Florida'), ('First Line Direct', 'First Line Direct'), ('First USA Bank', 'First USA Bank'), ('Fifth Third Bank', 'Fifth Third Bank'), ('First Citizens BancShares', 'First Citizens BancShares'), ('Fulton Financial Corporation', 'Fulton Financial Corporation'), ('First Hawaiian Bank', 'First Hawaiian Bank'), ('First Horizon National Corporation', 'First Horizon National Corporation'), ('Frost Bank', 'Frost Bank'), ('First Midwest Bank', 'First Midwest Bank'), ('Goldman Sachs', 'Goldman Sachs'), ('Grandeur Financials', 'Grandeur Financials'), ('HSBC Bank USA', 'HSBC Bank USA'), ('Home BancShares Conway', 'Home BancShares Conway'), ('Huntington Bancshares', 'Huntington Bancshares'), ('Investors Bank', 'Investors Bank'), ('??ntercity State Bank', '??ntercity State Bank'), ('KeyCorp', 'KeyCorp'), ('MB Financial', 'MB Financial'), ('Mizuho Financial Group', 'Mizuho Financial Group'), ('Midfirst Bank', 'Midfirst Bank'), ('M&T Bank', 'M&T Bank'), ('MUFG Union Bank ', 'MUFG Union Bank'), ('Morgan Stanley', 'Morgan Stanley'), ('Northern Trust', 'Northern Trust'), ('New  York Community Bank', 'New York Community Bank'), ('Old National Bank', 'Old National Bank'), ('Pacwest Bancorp', 'Pacwest Bancorp'), ('Pinnacle Financial Partners', 'Pinnacle Financial Partners'), ('PNC Financial Services', 'PNC Financial Services'), ('Raymond James Financial', 'Raymond James Financial'), ('RBC Bank', 'RBC Bank'), ('Region Financial Corporation', 'Region Financial Corporation'), ('Satander Bank', 'Satander Bank'), ('Synovus Columbus', 'Synovus Columbus'), ('Synchrony Financial', 'Synchrony Financial'), ('Sterling Bancorp', 'Sterling Bancorp'), ('Simmons Bank', 'Simmons Bank'), ('South State Bank', 'South State Bank'), ('Stifel St. Louise', 'Stifel St. Louise'), ('Suntrust Bank', 'Suntrust Bank'), ('TCF Financial Corporation', 'TCF Financial Corporation'), ('TD Bank', 'TD Bank'), ('The Bank of New York Mellon', 'The Bank of New York Mellon'), ('Texas Capital Bank', 'Texas Capital Bank'), ('UMB Financial Corporation', 'UMB Financial Corporation'), ('Utrecht-America', 'Utrecht-America'), ('United Bank', 'United Bank'), ('USAA', 'USAA'), ('U.S Bank', 'U.S Bank'), ('UBS', 'UBS'), ('Valley National Bank', 'Valley National Bank'), ('Washington Federal', 'Washington Federal'), ('Western Alliance Banorporation', 'Western Alliance Bancorporation'), ('Wintrust Financial', 'Wintrust Finacial'), ('Webster Bank', 'Webster Bank'), ('Wells Fargo', 'Wells Fargo'), ('Zions Bancorporation', 'Zions Bancorporation'), ('Other Bank', 'Other Bank')], max_length=250, null=True, verbose_name='Your Bank Name')),
                ('account_no', models.CharField(max_length=13, null=True, validators=[django.core.validators.RegexValidator(code='Invalid_input, Only Integers', message='Must Contain Numbers Only', regex='^[0-9]*$')], verbose_name='Recipient Account Number')),
                ('routing_no', models.CharField(blank=True, help_text='must be the recipients 9 digits routing number', max_length=13, null=True, validators=[django.core.validators.RegexValidator(code='Invalid_input, Only Integers', message='Must Contain Numbers Only', regex='^[0-9]*$')], verbose_name='Recipient Routing Number')),
                ('phone', models.CharField(blank=True, help_text='Example: 1234567890 (10 digits only)', max_length=10, null=True, unique=True, validators=[django.core.validators.RegexValidator(code='Invalid_input, Only Integers', message='Must Contain Numbers Only', regex='^[0-9]*$')], verbose_name='Contact 10 digit Phone Number')),
                ('nationality', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='countries_plus.country')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userprofile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Profile',
                'verbose_name_plural': 'User Profiles',
                'ordering': ['-modified'],
            },
        ),
    ]
