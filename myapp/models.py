from django.db import models


from django.contrib.auth.forms import AuthenticationForm
# Create your models here.
class Querry(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    number=models.CharField(max_length=50)
    address=models.TextField()
    zip_code=models.CharField(max_length=50)
    order_description=models.TextField()

    def __str__(self):
        return self.email
class customers(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=20)     
    re_enter_password=models.CharField(max_length=20)
     
    def __str__(self):
        return self.name

# login views  function       
