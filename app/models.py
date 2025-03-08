from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=100)
    budget = models.IntegerField()
    desc = models.TextField()

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    is_collected = models.BooleanField(default=False)
    price = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="items")



