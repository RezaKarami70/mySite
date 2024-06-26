from django import forms
from website.models import Contact,newsletter
from captcha.fields import CaptchaField

class NameForm(forms.Form):
    name = forms.CharField(max_length=255, label= "your name")
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)


class ContactForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = '__all__'
        
        

class newsletterForm(forms.ModelForm):
    class Meta:
        model = newsletter
        fields = '__all__'
    