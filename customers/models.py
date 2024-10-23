from django.db import models
from leads.models import Lead

# after lead converts to Customer
class Customer(models.Model):
    lead_id = models.ForeignKey(Lead,on_delete=models.CASCADE)
    org_name = models.CharField(max_length= 50)
    contact_name= models.CharField(max_length= 50)
    phone_number = models.CharField(max_length= 10)
    email = models.EmailField(max_length= 50,null= True) 
    conversation_date = models.DateField()
    renewal_date = models.DateField()
    start_date = models.DateField()
    subscription_used_date = models.DateField(max_length= 10)
    payment_cycle = models.CharField(max_length= 10)
    gst_no = models.CharField(max_length= 50)
    created_at = models.DateTimeField('created at', auto_now_add=True)
    updated_at = models.DateTimeField('updated at', auto_now=True) 

    def __str__(self):
        return f"{self.org_name}"


class Customer_communication(models.Model):
    customer_id = models.ForeignKey("Customer",on_delete=models.CASCADE)
    message = models.CharField(max_length= 500)
    created_at = models.DateTimeField('created at', auto_now_add=True)
    updated_at = models.DateTimeField('updated at', auto_now=True) 

    def __str__(self):
        return f"{self.customer_id.lead_id.first_name} {self.customer_id.lead_id.last_name}"