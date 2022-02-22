from django import  forms


class SearchForm(forms.Form):
    searchfield = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class':'form-control'})
    )

