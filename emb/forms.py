from django import forms
from django.contrib.auth.models import User
from . import models


class CustomerUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

class CustomerForm(forms.ModelForm):
    username = forms.CharField(max_length=40)
    email = forms.EmailField(max_length=40)

    class Meta:
        model = models.Customer
        fields = ['username', 'email', 'address', 'mobile']

    def save(self, commit=True):
        # First, save the User instance
        user = User(
            username=self.cleaned_data['username'],
            first_name=self.cleaned_data.get('first_name', ''),
            last_name=self.cleaned_data.get('last_name', ''),
            email=self.cleaned_data['email'],
        )
        if commit:
            user.set_password(self.cleaned_data['password'])  # Set password if provided
            user.save()

        # Now save the Customer instance
        customer = super().save(commit=False)
        customer.user = user  # Link the Customer to the User
        if commit:
            customer.save()
        return customer

class ProductForm(forms.ModelForm):
    class Meta:
        model=models.Product
        fields=['name','price','description','product_image']

#address of shipment
class AddressForm(forms.Form):
    Email = forms.EmailField()
    Mobile= forms.IntegerField()
    Address = forms.CharField(max_length=500)

class FeedbackForm(forms.ModelForm):
    class Meta:
        model=models.Feedback
        fields=['name','feedback']

#for updating status of order
class OrderForm(forms.ModelForm):
    class Meta:
        model=models.Orders
        fields=['status']

#for contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))


#Quote form
from django import forms

class QuoteForm(forms.Form):
    design_name = forms.CharField(max_length=255, label='Design Name')
    placement = forms.CharField(max_length=255, label='Placement')
    garment = forms.CharField(max_length=255, label='Garment')
    size = forms.CharField(max_length=255, label='Size')
    mail_id = forms.EmailField(label='Mail ID')
    confirm_mail_id = forms.EmailField(label='Confirm Mail ID')
    contact_no = forms.CharField(max_length=20, label='Contact No')

    def clean(self):
        cleaned_data = super().clean()
        mail_id = cleaned_data.get('mail_id')
        confirm_mail_id = cleaned_data.get('confirm_mail_id')
        if mail_id != confirm_mail_id:
            raise forms.ValidationError("Mail ID and Confirm Mail ID do not match")
        return cleaned_data