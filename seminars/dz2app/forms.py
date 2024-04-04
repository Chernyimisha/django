from django import forms
from dz2app.models import Customer, Order, Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name', 'description', 'price', 'volume', 'date', 'image',
        ]


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'name', 'email', 'phone', 'address', 'registration_date',
        ]


class OrderForm(forms.Form):
    customer = forms.ModelChoiceField(label="Покупатель", queryset=Customer.objects.all())
    products = forms.ModelMultipleChoiceField(label="Выбор товара", queryset=Product.objects.all(),
                                              widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}))


