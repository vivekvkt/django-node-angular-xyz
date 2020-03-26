from django.db import models

class Item(models.Model):
    item_name = models.CharField(max_length=255)
    item_desc= models.CharField(max_length=255)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500 ,default="https://image.flaticon.com/icons/svg/1377/1377194.svg")
    
    
    def __str__(self):
        return self.item_name
    
