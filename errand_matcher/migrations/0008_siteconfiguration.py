# Generated by Django 3.0.4 on 2020-04-22 22:05

from django.db import migrations, models
import phonenumber_field.modelfields
import phonenumbers


def make_phone_numbers_valid(apps, schema_editor):
    Volunteer = apps.get_model('errand_matcher', 'Volunteer')
    for v in Volunteer.objects.all():
        if not phonenumbers.is_valid_number(v.mobile_number):
            with_country_code = '+1{}'.format(v.mobile_number.raw_input)
            valid_number = phonenumbers.parse(with_country_code)
            v.mobile_number = valid_number
            v.save()


class Migration(migrations.Migration):

    dependencies = [
        ('errand_matcher', '0007_errand_requestor'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_number_on_call', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
            ],
        ),
        migrations.RunPython(make_phone_numbers_valid)
    ]
