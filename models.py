from django.db import models

from django_timestamps.softDeletion import SoftDeletionModel
from django_timestamps.timestamps import TimestampsModel

# Create your models here.
class CompanyModel(SoftDeletionModel, TimestampsModel):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, help_text="name of the company")
    bic = models.CharField(max_length=150, null=True, blank=True)

    class Meta:
        db_table = "companies"

class ContactModel(SoftDeletionModel, TimestampsModel):
    contact_id = models.AutoField(primary_key=True)
    company_id = models.ForeignKey(
        "CompanyModel", related_name="contacts", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(null=True, blank=True)

    class Meta:
        db_table = "contacts"

class OrderModel(SoftDeletionModel, TimestampsModel):
    order_id = models.AutoField(primary_key=True)
    order_number = models.CharField(max_length=150)
    company_id = models.ForeignKey("CompanyModel", related_name="orders", on_delete=models.CASCADE)
    contact_id = models.ForeignKey("ContactModel", related_name="orders", on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=18, decimal_places=9)
    order_date = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        db_table = "orders"


