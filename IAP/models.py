from django.db import models

class Purchace(models.Model):
    id = models.BigIntegerField(primary_key=True, auto_created=True)
    source = models.CharField(max_length= 50)
    product_id = models.TextField()
    purchase_id = models.TextField()
    localverificationdata = models.TextField()
    serververificationdata = models.TextField()
    purchace_date = models.DateTimeField(auto_now_add=True)
    purchace_price = models.CharField(max_length= 50)

    class Meta:
        managed = False
        app_label = "default"
        db_table = 'IAP_purchace'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class User(models.Model):
    id = models.BigIntegerField(primary_key=True, auto_created=True)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45, db_column='pass')
    isPurchace = models.IntegerField()

    class Meta:
        managed = False
        app_label = "service"
        db_table = 'test_user'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
