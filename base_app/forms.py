# from django import forms
# from .models import Profile

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['name', 'title', 'email', 'phone', 'birthday', 'location', 'image']
from django import forms

class ContactForm(forms.Form):
    fullname = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
