from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.http import JsonResponse
import json

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views import View
from django.views.generic import TemplateView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Product, Order, OrderItem,CustomerAddress, Customer
from .forms import EditAddressInfo, AddressForm, SearchForm

# Create your views here.


class LoginView(LoginView):
    fields = '__all__'
    template_name = 'myapp/loginview.html'
    # success_url = reverse_lazy('lists')
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('homepage')

class RegistrationView(FormView):
    # fields = '__all__'
    form_class = UserCreationForm
    template_name = 'myapp/register.html'
    success_url = reverse_lazy('homepage')

    def form_valid(self, form): # "form-valid" function is always "do" after submitting the form
        user = form.save()
        username = form.cleaned_data.get('username')
        Customer.objects.create(
                user = user,
                name = username, 
            )
        if user is not None:    # this mean "if the user successfully created..." or there is nothing left null required fields!!!
            login(self.request, user)   # this login function is for "authenticated" new user!!!
        return  super(RegistrationView, self).form_valid(form)
    
    def get(self, *args, **kwargs): # This takes responsibility to "redirect" to home if user is authenticated from registration page(do not see registration page)!!! for more remover this function and see changes!!!
        if self.request.user.is_authenticated:
            return redirect('homepage')
        return super(RegistrationView, self).get(*args, **kwargs)
    

class GuestPageView(ListView):
    model = Product
    template_name = 'myapp/guest.html'

class Searchpage(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'myapp/searchpage.html'

    def get_context_data(self, **kwargs):
        form = SearchForm(self.request.GET)
        mysearch = self.request.GET.get('search', False)
        check = Product.objects.filter(category__icontains=mysearch)
        catpro = Product.objects.filter(category__icontains=mysearch).order_by('-price')
        if check:
            print(check)
        else:
            print(bool(0))
        pro = Product.objects.all()
        order, created = Order.objects.get_or_create(customer = self.request.user.customer, complete=False)
        cartItems = order.get_cart_items
        form = SearchForm()
        context = {
            'catpro':catpro,
            'pro':pro,
            'check':check,
            'mysearch':mysearch,
            'cartItems': cartItems,
            'form':form
        }
        return context
    
class HomePageView(LoginRequiredMixin, ListView):
    model = Product
    # context_object_name = 'pro'/
    template_name = 'myapp/homepage.html'

    def get_context_data(self, **kwargs):
        form = SearchForm(self.request.GET)
        mysearch = self.request.GET.get('search', False)
        check = Product.objects.filter(category__icontains=mysearch)
        catpro = Product.objects.filter(category__icontains=mysearch).order_by('-price')
        if check:
            print(check)
        else:
            print(bool(0))
        pro = Product.objects.all()
        order, created = Order.objects.get_or_create(customer = self.request.user.customer, complete=False)
        cartItems = order.get_cart_items
        form = SearchForm()
        context = {
            'pro':pro,
            'check':check,
            'cartItems': cartItems,
            'form':form
        }
        return context
    

class CartPageView(LoginRequiredMixin, ListView):
    model = Order
    # context_object_name = 'carts'
    template_name = 'myapp/cartpage.html'

    # ---------------This was really amzing but it works only for single model menstioned inside class-------------

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['carts'], created = context['carts'].get_or_create(customer = self.request.user.customer, complete=False)
    #     context['carts'] = context['carts'].orderitem_set.all()
    #     return context

    def get_context_data(self, **kwargs):
        order, created = Order.objects.get_or_create(customer = self.request.user.customer, complete=False)
        carts = order.orderitem_set.all()
        cartItems = order.get_cart_items
        context = {
            'carts':carts,
            'order':order,
            'cartItems': cartItems
        }
        return context    


class CartDeleteView(LoginRequiredMixin, DeleteView):
    model = OrderItem
    context_object_name = 'carts'
    success_url = reverse_lazy('homepage')

class CartUpdateView(LoginRequiredMixin, View):
    def get(self, request):
        return JsonResponse({'message': 'Item was added'})
        # return JsonResponse("Item was added", safe=False)
    def post(self, request):
        data = json.loads(request.body)
        productId = data['productId']
        action = data['action']

        print('productid:',productId)
        print('action:',action)

        product = Product.objects.get(id=productId)
        order, created = Order.objects.get_or_create(customer=request.user.customer, complete=False)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

        if action == 'add':
            orderItem.quantity = orderItem.quantity + 1
        elif action == 'remove':
            orderItem.quantity = orderItem.quantity - 1
        
        orderItem.save()

        if orderItem.quantity <= 0:
            orderItem.delete()

        return JsonResponse({'message': 'Item was added'})
    

class CheckoutPageView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'myapp/checkout.html'

    def get_context_data(self, **kwargs):
        order, created = Order.objects.get_or_create(customer = self.request.user.customer, complete=False)
        checkout = order.orderitem_set.all()
        cartItems = order.get_cart_items
        form = EditAddressInfo()
        customadd = CustomerAddress.objects.filter(customer=self.request.user.customer)
        context = {
            'checkout':checkout,
            'order':order,
            'form':form,
            'address':customadd,
            'cartItems': cartItems
        }
        return context    
    
class SubmitInfo(LoginRequiredMixin, View):
    def get(self, request):
        return redirect('checkout')
    def post(self, request):
        order, created = Order.objects.get_or_create(customer=request.user.customer, complete=False)
        form = EditAddressInfo(request.POST)
        address = request.POST['address']
        city = request.POST['city']
        zipcode = request.POST['postal_code']
        mobile = request.POST['phonenumber']
        email = request.POST['email']
        editaddressinfo, created = CustomerAddress.objects.get_or_create(
            customer = self.request.user.customer,
            order = order,
        )
        editaddressinfo.save()
        editaddressinfo = CustomerAddress.objects.filter(
            customer = self.request.user.customer,
            order = order,
        ).update(
            customer = self.request.user.customer,
            order = order,
            address = address,
            city = city,
            postal_code = zipcode,
            phone_number = mobile,
            email = email
        )
        return redirect('checkout')

# The unique value of the phone number is big challenge