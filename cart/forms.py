from django import forms


class AddToCartProductForm(forms.Form):
    COUNT_CHOICES = [(i, str(i))for i in range(1, 30)]
    count = forms.TypedChoiceField(choices=COUNT_CHOICES, coerce=int)
    inplace = forms.BooleanField(required=False, widget=forms.HiddenInput)