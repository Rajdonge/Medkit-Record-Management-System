from django.db import models
from datetime import date, datetime, timedelta
from django.db.models import Q
# Create your models here.


class Information(models.Model):
    medicine_name = models.CharField(max_length=30)
    expiry_date = models.DateField(
        error_messages={'invalid': 'Please enter in "YYYY-MM-DD" Format!'})
    quantity = models.IntegerField(
        error_messages={'invalid': 'Please enter numbers!'})
    marked_price = models.FloatField(
        error_messages={'invalid': 'Please enter numbers!'})
    description = models.CharField(max_length=30, default="")
    discount = models.FloatField(
        error_messages={'invalid': 'Please enter numbers!'})
    company = models.CharField(max_length=30)
    dealer = models.CharField(max_length=30)

    def is_expiring_soon(self):
        expiry_date_range = (self.expiry_date, self.expiry_date + timedelta(days=20))

        expiring_objects = Information.objects.filter(Q(expiry_date = expiry_date_range[0]))

        return expiring_objects

class Sale_Information(models.Model):
    medicine_name = models.CharField(max_length=30)
    quantity = models.IntegerField(
        error_messages={'invalid': 'Please enter numbers!'})
    marked_price = models.FloatField(
        error_messages={'invalid': 'Please enter numbers!'})
    discount = models.FloatField(
        error_messages={'invalid': 'Please enter numbers!'})
    sale_id = models.ForeignKey(Information, on_delete=models.CASCADE)



