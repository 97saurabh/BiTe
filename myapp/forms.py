from django import forms
from django.contrib.auth.models import User
from myapp.models import UserProfileInfo,Food



class UserForm(forms.ModelForm):
    #username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    ##first_name= forms.CharField()
    #last_name= forms.CharField()
    #email = forms.EmailField()
    class Meta():
        model=User
        fields = ('username','password','first_name','last_name','email')
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model=UserProfileInfo
        fields = ('type_user',)
class FoodForm(forms.ModelForm):
    class Meta():
        model=Food
        fields = ('food_name','food_type','food_rate')
