
from django.db import models
from django.contrib.auth.models import User

class Property(models.Model):
    PROPERTY_TYPES = [
        ('Buy', 'Buy'),
        ('Rent', 'Rent'),
    ]

    name = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField(upload_to='property_images/', null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    property_type = models.CharField(max_length=4, choices=PROPERTY_TYPES, default='Buy')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'properties'
