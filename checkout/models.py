import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from programs.models import Program
from profiles.models import UserProfile

class Order(models.Model):

    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    

    def _generate_order_number(self):
        """ generate random and unique order number"""

        return uuid.uuid4().hex.upper()

    def update_total(self):
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.grand_total = self.order_total
        self.save()
    
    def save(self, *args, **kwargs):

        """ override original save method to set the order number if not set already"""

        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    
    def __str__(self):
        return self.order_number

class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    program = models.ForeignKey(Program, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):

        """ override original save method to set the lineitem total and update the order total """


        self.lineitem_total = self.program.price * self.quantity
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.program} on order {self.order.order_number}'
