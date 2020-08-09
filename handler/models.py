from django.db import models
from datetime import datetime

# Create your models here.
class RequestList(models.Model):
    request_type = models.CharField(max_length=100)
    request_desc = models.CharField(max_length=500)
    request_date = models.DateField(auto_created=True, default=datetime.now().date())
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    pin_code = models.CharField(max_length=6)
    status = models.CharField(max_length=100, default='Open')
    remarks = models.CharField(max_length=500, null=True)
    mobile_number = models.CharField(max_length=15, verbose_name="Alternate Phone number", default="N/A")

class RequestType(models.Model):
    type = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.type

class IndianStates(models.Model):
    state = models.CharField(max_length=25, primary_key=True)

    def __str__(self):
        return self.state

class StatusList(models.Model):
    status = models.CharField(max_length=20, primary_key=True)

    def __str__(self):
        return self.status
