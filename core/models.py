from django.conf import settings
from django.db import models

# Create your models here.
COLLECTIONS = (
        ('M', 'Men'),
        ('W', 'Women'),
        ('C', 'Children'),
    )


SIZES = (
    ('XS', 'XS'),
    ('S', 'S'),
    ('M', 'M'),
    ('L', 'L'),
    ('XL', 'XL'),
    ('XXL', 'XXL'),
)

STYLES = (
    ('TR', 'Trendy'),
    ('S', 'Summer'),
    ('H', 'Holiday'),
    ('OW', 'Office wear'),
    ('T', 'Traditional'),
)



#Collections groups for each collection
class Collection(models.Model):
    collection = models.CharField(max_length=10, choices=COLLECTIONS)

    def __str__(self):
        return self.collection

#style group for 
class Style(models.Model):
    style = models.CharField(max_length=20, choices=STYLES)

    def __str__(self):
        return self.style

class Item(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=20, db_index=True)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    style = models.ForeignKey(Style, on_delete=models.CASCADE)
    price = models.FloatField()
    size = models.CharField(max_length=20, choices=SIZES)
    description = models.TextField()
    image = models.FileField()

    def __str__(self):
        return self.name + ' '+ str(self.price)

    def __unicode__(self):
        return self.name


class CartItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.item


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


