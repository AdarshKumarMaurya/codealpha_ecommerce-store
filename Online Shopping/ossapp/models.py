from django.db import models

#category= models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=6)
    address=models.TextField()
    pincode=models.IntegerField()
    contactno=models.CharField(max_length=15)
    emailaddress=models.EmailField(max_length=50,primary_key=True)
    password = models.CharField(max_length=20, null=True)
    regdate=models.DateTimeField(auto_now_add=True)
    def is_exists(self):
        if Customer.objects.filter(emailaddress=self.emailaddress):
            return True
        else:
            False




class Login(models.Model):
    userid=models.CharField(max_length=50,primary_key=True)
    password=models.CharField(max_length=20)
    usertype=models.CharField(max_length=30)

class Category(models.Model):
    name= models.CharField(max_length=50)
    def __str__(self):
        return self.name
    @staticmethod
    def get_all_category():
        return Category.objects.all()


class Product(models.Model):
    name= models.CharField(max_length=50)
    price= models.IntegerField(default=0)
    desc =models.CharField(max_length=200)
    category= models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    image= models.ImageField(upload_to='newproducts/')
    @staticmethod
    def get_all_products():
        return Product.objects.all()
    @staticmethod
    def get_products_by_categoryid(category_id):
        return Product.objects.filter(category=category_id)