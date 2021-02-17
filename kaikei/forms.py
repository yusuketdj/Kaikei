from django import forms
from .models import Customer, Choice

class CustomerCreateForm(forms.ModelForm):
    
    class Meta:
        model = Customer
        exclude = (
            'is_waiting',
        )

class CustomerUpdateForm(forms.ModelForm):

    class Meta:
        model = Customer
        exclude = {
            'customer_id',
            'name',
        }

class ChoiceCreateForm(forms.ModelForm):

    class Meta:
        model = Choice
        exclude = (
            'hoken_total_score',
            'jiseki_total_score',
            'buturyou_total_score',
            'shouhin_total_score',
            'total_score',
        )

class CustomerSearchForm(forms.Form):
    customer_id = forms.IntegerField(label='顧客ID', required=True, widget=forms.TextInput(attrs={'class': 'input'}))