from django.db import models
from django.contrib.auth.models import User
from accounts.models import Interest
from accounts.models import Country

class Message(models.Model):
    topic = models.CharField(max_length=100, null=False, unique=False, blank=False)
    body = models.TextField(null=True, unique=False, blank=True)
    autor = models.ForeignKey(User, null=False, related_name='mess_autor')
    reader = models.ForeignKey(User, null=False, related_name='mess_reader')
    sent_date = models.DateField(null=True, blank=True)
    read_date = models.DateField(null=True, blank=True)
    price = models.IntegerField(max_length=10, null=True, unique=False, blank=True)
    interests = models.ManyToManyField(Interest)
    phone = models.CharField(max_length=20, null=True, unique=True, blank=True)
    first_name = models.CharField(max_length=20, null=True, unique=False, blank=True)
    last_name = models.CharField(max_length=20, null=True, unique=False, blank=True)
    middle_name = models.CharField(max_length=20, null=True, unique=False, blank=True)
    married = models.BooleanField(blank=True)
    birthday = models.DateField(null=True, blank=True)
    organisation = models.CharField(max_length=128, null=True, unique=False, blank=True)
    politic = models.CharField(max_length=128, null=True, unique=False, blank=True)
    religion = models.CharField(max_length=128, null=True, unique=False, blank=True)
    addr_index = models.IntegerField(max_length=15, null=True, unique=False, blank=True)
    addr_country = models.ForeignKey(Country, null=True, related_name='mess_country')
    addr_region = models.CharField(max_length=64, null=True, unique=False, blank=True)
    addr_area = models.CharField(max_length=64, null=True, unique=False, blank=True)
    addr_city = models.CharField(max_length=64, null=True, unique=False, blank=True)
    addr_home = models.CharField(max_length=64, null=True, unique=False, blank=True)
    addr_MO = models.CharField(max_length=64, null=True, unique=False, blank=True)
    gps =  models.CharField(max_length=20, null=True, unique=False, blank=True)