from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
User_CHOICES = (
    ('shop','Vendor'),
    ('buyer', 'Customer')
)
class UserProfileInfo(models.Model):
    user=models.OneToOneField(User,on_delete='CASCADE',related_name='type')
    type_user=models.CharField(max_length=10, choices=User_CHOICES,blank=False)


class Food(models.Model):
    user=models.ForeignKey('auth.User',on_delete='CASCADE',related_name='foods')
    food_name=models.CharField(max_length=25,blank=False)
    food_type=models.CharField(max_length=25)
    food_rate=models.PositiveIntegerField()
    def get_absolute_url(self):
        return reverse('myapp:food_list')
class Add_to_cart(models.Model):
    customer=models.ForeignKey('auth.User',on_delete='CASCADE',related_name='customer')
    vendor=models.ForeignKey(Food,on_delete="",related_name='vendors')
class Orders(models.Model):
    customer=models.CharField(max_length=25)
    vendor=models.CharField(max_length=25)
    food_name=models.CharField(max_length=25)
    food_rate=models.CharField(max_length=25)
    food_type=models.CharField(max_length=25)
    order_status=models.CharField(max_length=25)
    date_field=models.DateField(auto_now=True)
