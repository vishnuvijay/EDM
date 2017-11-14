# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# Database Tables should be defined as class object
class Customer(models.Model):
    CustomerId          = models.IntegerField(unique=True)
    CustomerName        = models.CharField(max_length=200)

class Donors(models.Model):
    OrganizationName    = models.CharField(max_length=100)
    Salutation          = models.CharField(max_length=100)
    FirstName           = models.CharField(max_length=100)
    LastName            = models.CharField(max_length=100)
    Email               = models.EmailField(max_length=100)
    PhoneNumber         = models.CharField(max_length=15)
    Comments            = models.CharField(max_length=100)
    StreetAddress       = models.CharField(max_length=100)
    City                = models.CharField(max_length=100)
    State               = models.CharField(max_length=100)
    Zip                 = models.CharField(max_length=100)
    ICS                 = models.CharField(max_length=2)

class SearchDonor(models.Model):

    SearchQuery        = models.CharField(max_length=255)
