from django.db import models

# Create your models here.



class Restaurant(models.Model):

    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    contact = models.CharField(max_length=15)
    email = models.EmailField(null=True, blank=True)

    rating = models.FloatField(default=0)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Dish(models.Model):

    name = models.CharField(max_length=200)

    description = models.TextField(null=True, blank=True)

    price = models.DecimalField(max_digits=6, decimal_places=2)

    quantity = models.IntegerField()   # instead of CharField

    is_available = models.BooleanField(default=True)

    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name="dishes"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name