from django.db import models

from account.models import CustomUser, Department


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    is_collected = models.BooleanField(default=False)
    price = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="items")
    item_image = models.ImageField(upload_to='item/')


class Note(models.Model):
    text = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="notes")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="notes")



