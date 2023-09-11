from django.db import models

class Purchace(models.Model):
    source = models.CharField(max_length= 50,)
    product_id = models.TextField()
    purchase_id = models.TextField()
    localverificationdata = models.TextField()
    serververificationdata = models.TextField()
    purchace_date = models.DateTimeField(auto_now_add=True)
    purchace_price = models.CharField(max_length= 50)
    
    def save(self, *args, **kwargs):
        
        super().save(*args, **kwargs)
