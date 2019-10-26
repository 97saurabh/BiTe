from django.shortcuts import render,get_object_or_404
from myapp.forms import UserForm,UserProfileInfoForm,FoodForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from myapp.models import UserProfileInfo,Food,Add_to_cart,Orders
from . import models
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.models import User
# Create your views here.
def about_us(request):

    return render(request,'myapp/aboutus.html',{})
def food_list(request):

    return render(request,'myapp/food_list.html',{})
def home(request):
    data = User.objects.all()



    return render(request,'myapp/base.html',{'data':data,})
def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)

        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile= profile_form.save(commit=False)
            profile.user=user

            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:

        user_form =UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'registration/registration.html',{
                                    'user_form':user_form,
                                    'profile_form':profile_form,
                                    'registered':registered,
    })
def user_login(request):
    if request.method=='POST':

        username=request.POST.get('username')

        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        #print("USER",user.first_name)
        if user:
            if user.is_active:
                login(request,user)
                #print("USER",UserProfileInfo.objects.get(user=user).type_user)
                return HttpResponseRedirect(reverse('myapp:home'))
            else:
                user=False
                return render(request,'registration/login.html',{'user':user})
        else:
            print("Some tried to fail")
            print("Username",username,"Pass",password)
            user=False
            return render(request,'registration/login.html',{'user':user})
    else:
        return render(request,'registration/login.html',{})
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('myapp:home'))
class FoodCreateView(LoginRequiredMixin,CreateView):
    #login_url='/login/'
    redirect_field_name = "food_list.html"
    form_class = FoodForm
    model = Food
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
class FoodUpdateView(LoginRequiredMixin,UpdateView):
    login_url='/login/'
    redirect_field_name = "food_list.html"
    form_class = FoodForm
    model = Food
class PostDeleteView(LoginRequiredMixin,DeleteView):

    model = Food
    success_url = reverse_lazy('myapp:food_list')



@login_required
def cart(request,pk):
    food = get_object_or_404(Food,pk=pk)
    print(food.food_name)
    print(food.user)
    print(request.user)
    c=Add_to_cart(customer=request.user,vendor=food)
    c.save()


    return HttpResponseRedirect(reverse('myapp:home'))
@login_required
def adding_to_cart(request,pk):
    data = Add_to_cart.objects.all()
    total=0
    for i in data:
        if i.customer==request.user:
            total=total+i.vendor.food_rate
        #else:
            #print(total)
            #print(i.customer,request.user.username,request.user)
            #total=789
    #print(i.vendor.food_name,i.vendor.food_rate,i.vendor.user)
    #print(request.user.username)
    #print(i.customer)
    #Add_to_cart.objects.all().delete()
    return render(request,'myapp/cart_added.html',{'data':data,'total':total,})
@login_required
def clear_cart(request,pk):
    Add_to_cart.objects.all().delete()
    return HttpResponseRedirect(reverse('myapp:home'))
@login_required
def order_creating(request,pk):
    #Orders.objects.all().delete()
    data = Add_to_cart.objects.all()
    for i in data:
        if i.customer==request.user:
            ob=Orders(customer=request.user,vendor=i.vendor.user,food_name=i.vendor.food_name,food_rate=i.vendor.food_rate,food_type=i.vendor.food_type,order_status="Pending")
            ob.save()
    Add_to_cart.objects.all().delete()
    return HttpResponseRedirect(reverse('myapp:your_order'))
@login_required
def your_orders(request):
    dat=Orders.objects.all()
    for data in dat:
        print(data.customer)
        print(data.vendor)
        print(data.food_name)
        print(data.food_rate)
        print(data.food_type)
        print(data.order_status)
        print(data.date_field)
        print()
    return render(request,'myapp/orders.html',{'data':dat,})
@login_required
def change_status(request,pk):
    a=Orders.objects.get(pk=pk)
    a.order_status="Completed"
    a.save()
    print(a.order_status)
    return HttpResponseRedirect(reverse('myapp:your_order'))
@login_required
def cart_delete(request,pk):
    Add_to_cart.objects.exclude(pk=pk)
    return HttpResponseRedirect(reverse('myapp:your_cart',kwargs={'pk':request.user.pk}))
