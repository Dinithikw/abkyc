# Generated by Django 2.2.10 on 2021-05-16 09:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kyc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalKyc_Info',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('salutation_temp', models.CharField(max_length=5)),
                ('full_name_temp', models.CharField(max_length=200)),
                ('name_init_temp', models.CharField(max_length=100)),
                ('profile_pic_temp', models.TextField(blank=True, max_length=100, null=True)),
                ('live_video_temp', models.TextField(max_length=100, null=True)),
                ('id_type_temp', models.CharField(max_length=50)),
                ('nics_no_temp', models.CharField(max_length=50)),
                ('date_of_birth_temp', models.CharField(max_length=20)),
                ('driv_lic_temp', models.CharField(blank=True, max_length=50, null=True)),
                ('driv_exp_temp', models.CharField(blank=True, max_length=20, null=True)),
                ('pass_no_temp', models.CharField(blank=True, max_length=50, null=True)),
                ('pass_exp_temp', models.CharField(blank=True, max_length=20, null=True)),
                ('birth_cernum_temp', models.CharField(blank=True, max_length=10, null=True)),
                ('post_id_temp', models.CharField(blank=True, max_length=10, null=True)),
                ('oafsc_temp', models.CharField(blank=True, max_length=10, null=True)),
                ('visa_copy_temp', models.TextField(blank=True, max_length=100, null=True)),
                ('othe_identity_doc_temp', models.TextField(blank=True, max_length=100, null=True)),
                ('nationality_temp', models.CharField(max_length=50)),
                ('nationality_other_temp', models.CharField(blank=True, max_length=50, null=True)),
                ('type_of_visa_temp', models.CharField(blank=True, max_length=20)),
                ('visa_exp_temp', models.CharField(blank=True, max_length=20, null=True)),
                ('other_types_temp', models.CharField(blank=True, max_length=20)),
                ('other_exp_temp', models.CharField(blank=True, max_length=20, null=True)),
                ('foreign_addre_temp', models.CharField(blank=True, max_length=200, null=True)),
                ('vari_doc_type_temp', models.CharField(blank=True, max_length=200, null=True)),
                ('vari_doc_temp', models.TextField(blank=True, max_length=100, null=True)),
                ('pep_person_temp', models.CharField(blank=True, max_length=200, null=True)),
                ('us_city_temp', models.CharField(blank=True, max_length=200, null=True)),
                ('resident_sri_temp', models.CharField(blank=True, max_length=10, null=True)),
                ('country_resident_temp', models.CharField(blank=True, max_length=50)),
                ('house_no_temp', models.CharField(max_length=20)),
                ('street_temp', models.CharField(max_length=20)),
                ('city_temp', models.CharField(max_length=20)),
                ('postal_code_temp', models.CharField(blank=True, max_length=10, null=True)),
                ('state_address_temp', models.CharField(blank=True, max_length=20, null=True)),
                ('house_no_per_temp', models.CharField(max_length=20)),
                ('street_per_temp', models.CharField(max_length=20)),
                ('city_per_temp', models.CharField(max_length=20)),
                ('postal_code_per_temp', models.CharField(blank=True, max_length=10, null=True)),
                ('mob_no_temp', models.CharField(max_length=20)),
                ('office_num_temp', models.CharField(blank=True, max_length=20, null=True)),
                ('home_num_temp', models.CharField(blank=True, max_length=20, null=True)),
                ('email_add_temp', models.CharField(blank=True, max_length=50, null=True)),
                ('email_add_verification', models.CharField(blank=True, max_length=50, null=True)),
                ('red_flag_temp', models.CharField(blank=True, max_length=5, null=True)),
                ('blue_flagadd_temp', models.CharField(blank=True, max_length=5, null=True)),
                ('blue_flag_temp', models.CharField(blank=True, max_length=5, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical kyc_ info',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
