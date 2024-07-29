from django.db import models
from inventory.models import Item

class Invoice(models.Model):
    invoice_number = models.CharField(max_length=50)
    invoice_date = models.DateField()
    invoice_amount = models.DecimalField(max_digits=10, decimal_places=2)
    invoice_status = models.CharField(max_length=50)
    invoice_description = models.CharField(max_length=200)
    invoice_file = models.FileField(upload_to='invoices/')
    invoice_created_at = models.DateTimeField(auto_now_add=True)
    invoice_updated_at = models.DateTimeField(auto_now=True)

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    service_type = models.CharField(max_length=50) # 'Appointment', 'Lab Test', 'Prescription'
    service_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    item_quantity = models.IntegerField()
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    item_created_at = models.DateTimeField(auto_now_add=True)
    item_updated_at = models.DateTimeField(auto_now=True)    
