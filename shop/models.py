from django.db import models 
from django.core.validators import MinValueValidator


class Shop(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Promotion(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    discount = models.FloatField()

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    unit_price = models.DecimalField(decimal_places=2, max_digits=6, 
                                    validators=[
                                    MinValueValidator(100, message='Unit price cannot be less than 100')])
    last_update = models.DateTimeField(auto_now=True)
    promotion = models.ManyToManyField(Promotion, blank=True)


    class Meta:
        ordering = ['-unit_price']

    def __str__(self):
        return self.title  

class Collection(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title 

class ShopCollection(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.collection.__str__()

class ShopProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    inventory = models.IntegerField()
    product_collection = models.ForeignKey(ShopCollection, on_delete=models.CASCADE)
    delivery_cost = models.DecimalField(decimal_places=2, max_digits=4, default=0.00)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.first_name

class Order(models.Model):
    PAYMENT_COMPLETE = 'C'
    PAYMENT_PENDING = 'P'
    PAYMENT_FAILED = 'F'

    PAYMENT_STATUS = [
        (PAYMENT_COMPLETE, 'COMPLETE'),
        (PAYMENT_PENDING, 'PENDING'),
        (PAYMENT_FAILED, 'FAILED')
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

class OrderItem(models.Model):
    product = models.ForeignKey(ShopProduct, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

class Cart(models.Model):
    placed_at = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

class CartItem(models.Model):
    quantity = models.PositiveSmallIntegerField()
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(ShopProduct, on_delete=models.CASCADE)