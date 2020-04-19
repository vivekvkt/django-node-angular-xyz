from django.conf import settings
from django.db import models

def upload_status_image(instance, filename):
    return "status/{user}/{filename}".format(user=instance.user,filename=filename)



class StatusQuerySet(models.Model):
    pass


class StatusManager(models.Model):
    def get_QuerySet(self):
        return StatusQuerySet(self.model, using=self._db)


class Status(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=upload_status_image, null=True,blank=True)
    updated = models.DateField(auto_now=True)
    timestamp = models.DateField(auto_now_add=True)
    
    object = StatusManager()
    
    
    def __str__(self):
        return str(self.content)[:50]
    
    
    class Meta:
        verbose_name = 'Status post'
        verbose_name_plural='Status posts'
# Create your models here.
