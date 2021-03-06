# Generated by Django 3.0.4 on 2020-03-27 22:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('errand_matcher', '0003_volunteer_mobile_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfirmationToken',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Requestor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
