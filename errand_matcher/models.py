from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import uuid
import math
import random

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'volunteer'),
        (2, 'requestor')
    )

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=1)


# Create your models here.
class Volunteer(models.Model):
    FREQUENCY_CHOICES = (
        (1, 'anytime'),
        (2, '2-3 times per week'),
        (3, 'once a week')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    mobile_number = PhoneNumberField(default='555-555-5555')
    lon = models.FloatField()
    lat = models.FloatField()
    frequency = models.PositiveSmallIntegerField(choices=FREQUENCY_CHOICES)
    walks = models.BooleanField()
    has_bike = models.BooleanField()
    has_car = models.BooleanField()
    speaks_spanish = models.BooleanField()
    speaks_chinese = models.BooleanField()
    speaks_russian = models.BooleanField()
    # Certified that Volunteer has read Health and Safety Protocol
    consented = models.BooleanField()
    opted_out = models.BooleanField(default=False)

    def __str__(self):
        return '{} {}'.format(self.user.first_name, 
            self.user.last_name)

class Requestor(models.Model):
    CONTACT_PREFERENCE_CHOICES = (
        (1, 'sms'),
        (2, 'call')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    mobile_number = PhoneNumberField()
    date_of_birth = models.DateField()
    lon = models.FloatField()
    lat = models.FloatField()
    address_str = models.CharField(default='', max_length=1024)
    apt_no = models.CharField(default='', max_length=8)
    contact_preference = models.PositiveSmallIntegerField(choices=CONTACT_PREFERENCE_CHOICES, default=1)

    def __str__(self):
        return '{} {}'.format(self.user.first_name, 
            self.user.last_name)

class SiteConfiguration(models.Model):
    mobile_number_on_call = PhoneNumberField()

class Errand(models.Model):
    STATUS_CHOICES = (
        (1, 'open'),
        (2, 'in progress'),
        (3, 'complete'),
        (4, 'failed')
    )

    URGENCY_CHOICES = (
        (1, 'less than 24 hours'),
        (2, 'within 3 days')
    )

    REVIEW_CHOICES = (
        (1, 'positive'),
        (2, 'negative')
    )

    requested_time = models.DateTimeField()
    claimed_time = models.DateTimeField(blank=True, null=True)
    completed_time = models.DateTimeField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES)
    urgency = models.PositiveSmallIntegerField(choices=URGENCY_CHOICES)
    requestor = models.ForeignKey(Requestor, on_delete=models.CASCADE)
    request_round = models.PositiveSmallIntegerField(default=0)
    claimed_volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE, related_name='claimed_volunteer', blank=True, null=True)
    contacted_volunteers = models.ManyToManyField(Volunteer, related_name='contacted_volunteers', blank=True)
    requestor_review = models.PositiveSmallIntegerField(choices=REVIEW_CHOICES, blank=True, null=True)
    volunteer_review = models.PositiveSmallIntegerField(choices=REVIEW_CHOICES, blank=True, null=True)
    additional_info = models.TextField(blank=True, null=True)
    access_id = models.UUIDField(blank=True, null=True)

class UserOTP(models.Model):
    def generate_token():
        digits_in_otp = '0123456789'

        token = ''
        for i in range(6):
            token += digits_in_otp[math.floor(random.random() * 10)] 

        return token

    mobile_number = PhoneNumberField()
    token = models.CharField(default=generate_token(), max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)






