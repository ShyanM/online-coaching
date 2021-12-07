from django.db import models

# Create your models here.
class Program(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()
    equipment = models.TextField()
    included = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name