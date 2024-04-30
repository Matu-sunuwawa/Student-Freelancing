from django import forms
from .models import CustomerAddress

class EditAddressInfo(forms.Form):
    address = forms.Field(widget=forms.TextInput(attrs={'class':'form-control','name':'address','placeholder':'Enter your street address'}))
    city = forms.Field(widget=forms.TextInput(attrs={'class':'form-control','name':'city','placeholder':'Enter your city/ketema'}))
    postal_code = forms.Field(
        label='Zipcode(Optional)',
        widget=forms.TextInput(attrs={'class':'form-control','name':'zipcode','placeholder':'Enter your Zipcode'}),
        required=False
        )
    phonenumber = forms.Field(
        widget=forms.TextInput(attrs={'class':'form-control','name':'phone','placeholder':'+251912345678'}),
        validators=["please enter the unique number!"]
        )
    email = forms.Field(widget=forms.TextInput(attrs={'class':'form-control','name':'email','placeholder':'Enter your email'}))


class AddressForm(forms.ModelForm):
    class Meta:
        model = CustomerAddress
        fields = ('customer','order','address','city','postal_code','phone_number','email')

        widget = {
            'customer': forms.TextInput(attrs={'class':'form-control'}),
            'order': forms.TextInput(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your Street Address'}),
            'city': forms.TextInput(attrs={'class':'form-control'}),
            'postal_code': forms.TextInput(attrs={'class':'form-control'}),
            'phone_number': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
        }


Level_CHOICES = (
        ('kg', 'Kg level'),
        ('E', 'Elementary level'),
        ('H', 'HighSchool level'),
        ('U', 'Undergraduate level'),
        ('M', 'Msc level'),
        ('P', 'Phd level'),
    )

class SearchForm(forms.Form):
    search = forms.ChoiceField(
        choices=Level_CHOICES,
        widget=forms.Select(attrs={'class':'form-control'}),
        required=True
    )