from django import forms
from blog.models import Comment
from captcha.fields import CaptchaField

class NameForm(forms.ModelForm):
    captcha = CaptchaField()
    name = forms.CharField(max_length=255, label= "your name")
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)
    
    
class CommentForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Comment
        fields = ['post', 'name', 'email', 'subject', 'message','captcha']