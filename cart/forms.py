from django import forms
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 31)]


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class": "form-control", "style":"width:60px;"})
    )
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)