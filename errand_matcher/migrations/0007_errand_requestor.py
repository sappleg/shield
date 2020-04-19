# Generated by Django 3.0.4 on 2020-04-09 23:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('errand_matcher', '0006_delete_requestor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requestor',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('mobile_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('date_of_birth', models.DateField()),
                ('lon', models.FloatField()),
                ('lat', models.FloatField()),
                ('contact_preference', models.PositiveSmallIntegerField(choices=[(1, 'sms'), (2, 'call')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Errand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requested_time', models.DateTimeField()),
                ('claimed_time', models.DateTimeField(blank=True, null=True)),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'open'), (2, 'in progress'), (3, 'complete'), (4, 'failed')])),
                ('urgency', models.PositiveSmallIntegerField(choices=[(1, 'less than 24 hours'), (2, 'within 3 days')])),
                ('requestor_review', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'positive'), (2, 'negative')], null=True)),
                ('volunteer_review', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'positive'), (2, 'negative')], null=True)),
                ('claimed_volunteer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='claimed_volunteer', to='errand_matcher.Volunteer')),
                ('contacted_volunteers', models.ManyToManyField(blank=True, related_name='contacted_volunteers', to='errand_matcher.Volunteer')),
                ('requestor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='errand_matcher.Requestor')),
            ],
        ),
    ]