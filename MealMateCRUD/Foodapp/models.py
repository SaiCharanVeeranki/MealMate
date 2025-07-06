from django.db import models
# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length = 100)
    item_desc = models.CharField(max_length = 100)
    price = models.IntegerField()
    item_image = models.URLField(default="https://e1.pngegg.com/pngimages/614/418/png-clipart-jsplaylist-loading-icon-thumbnail.png")