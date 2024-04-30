from django.test import TestCase

# Create your tests here.




# class SubmitInfo(LoginRequiredMixin, View):
#     def get(self, request):
#         return redirect('checkout')
#     def post(self, request):
#         order, created = Order.objects.get_or_create(customer=request.user.customer, complete=False)
#         if request.method == 'POST':
#             form = EditAddressInfo(request.POST)
#             address = request.POST['address']
#             city = request.POST['city']
#             zipcode = request.POST['postal_code']
#             mobile = request.POST['phonenumber']
#             email = request.POST['email']
#             editaddressinfo, created = CustomerAddress.objects.get_or_create(
#                 customer = self.request.user.customer,
#                 order = order,
#             )
#             editaddressinfo.save()
#             editaddressinfo = CustomerAddress.objects.filter(
#                 customer = self.request.user.customer,
#                 order = order,
#             ).update(
#                 customer = self.request.user.customer,
#                 order = order,
#                 address = address,
#                 city = city,
#                 postal_code = zipcode,
#                 phone_number = mobile,
#                 email = email
#             )
#             return redirect('checkout')
#         else:
#             form = EditAddressInfo()




# class SubmitInfo(LoginRequiredMixin, View):
#     def get(self, request):
#         old_data = {
#             'address':'adama',
#             'city':'adama',
#             'postal_code':'0000',
#             'phonenumber':'+251912345678',
#             'email':'g@gmail.com'
#         }
#         form = EditAddressInfo(initial=old_data)
#         ctx = {'forms':form}
#         return render(request, "myapp/checkout.html", ctx)
#     def post(self, request):
#         del form
#         order, created = Order.objects.get_or_create(customer=request.user.customer, complete=False)
#         if request.method == 'POST':
#             form = EditAddressInfo(request.POST)
#             address = request.POST['address']
#             city = request.POST['city']
#             zipcode = request.POST['postal_code']
#             mobile = request.POST['phonenumber']
#             email = request.POST['email']
#             editaddressinfo, created = CustomerAddress.objects.get_or_create(
#                 customer = self.request.user.customer,
#                 order = order,
#             )
#             editaddressinfo.save()
#             editaddressinfo = CustomerAddress.objects.filter(
#                 customer = self.request.user.customer,
#                 order = order,
#             ).update(
#                 customer = self.request.user.customer,
#                 order = order,
#                 address = address,
#                 city = city,
#                 postal_code = zipcode,
#                 phone_number = mobile,
#                 email = email
#             )

#             if not form.is_valid():
#                 ctx = {"forms":form}
#                 return render(request, "myapp/checkout.html", ctx)

#             return redirect('checkout')
#         else:
#             form = EditAddressInfo()