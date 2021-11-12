from django.db import models
from .utils import *
# Create your models here.
class link(models.Model):
    name=models.CharField(max_length=250,blank=True)
    url=models.URLField()
    current_price=models.FloatField(blank=True)
    old_price=models.FloatField(blank=True)
    difference_price=models.FloatField(blank=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering=('current_price','created')
    def save(self, *args, **kwargs):
       name3,price4=get_link_data(self.url)
       old_price=self.current_price
       if self.current_price:
           if price4 != old_price:
               differ=price4 - old_price
               self.difference_price=round(differ,2)
               self.old_price=old_price
       else:
            self.difference_price=0
            self.old_price=0
       self.name=name3
       self.current_price=price4
       super().save(*args, **kwargs) # Call the real save() method