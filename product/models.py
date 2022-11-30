from django.db import models


class Color(models.Model):
    """
    Model for product colors
    """
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Size(models.Model):
    """
    Model for product sizes (if available)
    """
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Product(models.Model):
    """
    Modal for products
    """
    title = models.CharField(max_length=30)
    description = models.TextField()
    price = models.IntegerField()
    discount = models.SmallIntegerField()
    image = models.ImageField(upload_to="products")
    size = models.ManyToManyField(Size, related_name="products",
                                  null=True, blank=True)
    color = models.ManyToManyField(Color, related_name="products")

    def __str__(self):
        return self.title
