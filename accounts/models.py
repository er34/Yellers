from django.db import models
from django.contrib.auth.models import User

class Interest(models.Model):
    name = models.CharField(max_length=100, null=False, unique=False, blank=False)
    parent =  models.ForeignKey('self', null=True, blank=True, related_name='this_parent')
    
    def __unicode__(self):
        return self.name;
    
class Kladr(models.Model):
    itype = models.IntegerField(max_length=1, null=False, unique=False, blank=False)
    iaddrcode = models.IntegerField(max_length=2, null=False, unique=False, blank=False)
    iareacode = models.IntegerField(max_length=3, null=False, unique=False, blank=False)
    icitycode = models.IntegerField(max_length=3, null=False, unique=False, blank=False)
    inpcode = models.IntegerField(max_length=3, null=False, unique=False, blank=False)
    istreetcode = models.IntegerField(max_length=4, null=False, unique=False, blank=False)
    icode = models.IntegerField(max_length=21, null=False, unique=False, blank=False)
    name = models.CharField(max_length=40, null=False, unique=False, blank=False)
    short = models.CharField(max_length=10, null=False, unique=False, blank=False)
    zipcode = models.CharField(max_length=7, null=False, unique=False, blank=False)
    anothernames = models.CharField(max_length=40, null=False, unique=False, blank=False)
    isactual = models.CharField(max_length=200, null=False, unique=False, blank=False)
    
    def __unicode__(self):
        return self.name;

class Country(models.Model):
    name = models.CharField(max_length=80, null=False, unique=False, blank=False)
      
    def __unicode__(self):
        return self.name;  

class Account(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(upload_to = 'avatars', max_length=2000, null=True, blank=True)
    email = models.EmailField()
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
    addr_country = models.ForeignKey(Country, null=True, related_name='acc_country')
    addr_region = models.CharField(max_length=64, null=True, unique=False, blank=True)
    addr_area = models.CharField(max_length=64, null=True, unique=False, blank=True)
    addr_city = models.CharField(max_length=64, null=True, unique=False, blank=True)
    addr_home = models.CharField(max_length=64, null=True, unique=False, blank=True)
    addr_MO = models.CharField(max_length=64, null=True, unique=False, blank=True)
    gps =  models.CharField(max_length=20, null=True, unique=False, blank=True)
    
    def __unicode__(self):
        return self.email;

class UInterest(models.Model):
    user = models.ForeignKey(Account, null=False, related_name='UI_user')
    interest = models.ForeignKey(Interest, null=False, related_name='UI_interest')
    recieve = models.BooleanField(default=True)
    popup = models.BooleanField(default=True)
    ring = models.BooleanField(default=True)
    price = models.IntegerField(max_length=10, null=True, unique=False, blank=True)
    
    
    
    