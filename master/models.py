from django.db import models

# Create your models here.
class BaseContent(models.Model):
    timestamp =models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)

class Category(BaseContent):
    name=models.CharField(max_length=225)

class SubCategory(BaseContent):
    subname=models.CharField(max_length=225)
    Category_id=models.ForeignKey(to=Category,on_delete=models.CASCADE)

# class AmenityMaster(BaseContent):
#     amenity_name = models.CharField(max_length=225)

# class Property(BaseContent):
#     name = models.CharField(max_length=225)
#     address = models.TextField()
#     amount = models.CharField(max_length=225)
#     currency = models.CharField(max_length=225)
#     description = models.TextField()