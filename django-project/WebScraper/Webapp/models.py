from django.db import models


class Link(models.Model):
    name = models.CharField(max_length=1000, null=True, blank=True)
    address_bar = models.CharField(max_length=1000, null=True ,blank=True)
   
    
    def __str__(self):
        return  self.name
