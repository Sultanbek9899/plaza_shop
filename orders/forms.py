from django import  forms
from .models import  Order


class OrderCheckoutForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = [
            'first_name',
            'last_name',
            'middle_name',
            'email',
            'phone_number',
            'address',
            'postal_code',
        ]
        forms_attrs = {
            "class":"form-control",
            'data-islam':"ISLAM",
        }
        widgets = {
            "first_name": forms.TextInput(attrs=forms_attrs),
            "last_name": forms.TextInput(attrs=forms_attrs),
            "middle_name": forms.TextInput(attrs=forms_attrs),
            'email':forms.EmailInput(attrs=forms_attrs),
            'phone_number':forms.TextInput(attrs=forms_attrs),
            'address': forms.TextInput(attrs=forms_attrs),
            "postal_code": forms.TextInput(attrs=forms_attrs),

        }
