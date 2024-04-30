from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Client(models.Model):
    phone = PhoneNumberField(null=False, blank=False, unique=True)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'customer', null=True, blank=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()


    def __str__(self):
        return self.name

class ShoppingCart(models.Model):
    customer = models.OneToOneField(Customer, related_name='shoppingcart', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    quantity = models.IntegerField(default=0, null=True, blank=True)


    def __str__(self):
        return self.product_name

class Product(models.Model):
    Level_CHOICES = (
        ('kg', 'Kg level'),
        ('Elementary', 'Elementary level'),
        ('HighSchool', 'HighSchool level'),
        ('Undergraduate', 'Undergraduate level'),
        ('Msc', 'Msc level'),
        ('Phd', 'Phd level'),
    )
    shoppingcart = models.ForeignKey(ShoppingCart, related_name='product', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=100, choices=Level_CHOICES)
    about = models.CharField(null=True,max_length=200)


    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class ProductCategory(models.Model):
    product = models.ManyToManyField(Product, blank=True)
    background = models.TextField()
    certificate = models.ImageField(null=True, blank=True)

    def __str__(self):
        count = self.background.split(" ")
        result = []
        for i in range(0,len(count)):
            if i<=3:
                result.append(count[i])
            else:
                result.append('....')
                break
        return ' '.join(result)

    # @property
    # def imageURL(self):
    #     try:
    #         url = self.image.url
    #     except:
    #         url = ''
    #     return url

class Variation(models.Model):
    product = models.ManyToManyField(Product, blank=True)
    sex = models.CharField(max_length=255, null=True, blank=True)
    religion = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.sex
    
class Payment(models.Model):
    customer = models.OneToOneField(Customer,related_name='payment', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    method = models.CharField(max_length=255, null=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.method
    
class Order(models.Model):
    customer = models.ForeignKey(Customer,related_name='order', on_delete=models.CASCADE, null=True, blank=False)
    complete = models.BooleanField(default=False)
    date_order = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total 

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total 
    
class OrderItem(models.Model):
	product = models.ForeignKey(Product, related_name='orderitem', on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total

        
class Discount(models.Model):
    order = models.OneToOneField(Order,related_name='discount', on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.value)
    
class CustomerAddress(models.Model):
    customer = models.ForeignKey(Customer,related_name='customeraddress', on_delete=models.CASCADE, null=True)
    order = models.ForeignKey(Order, related_name='customeraddress', on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=255, null=False)
    # timezone.now()
    city = models.CharField(max_length=255, null=False)
    postal_code = models.CharField(max_length=255, null=False)
    # phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    phone_number = PhoneNumberField(null=False, blank=False)
    email = models.EmailField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.phone_number)