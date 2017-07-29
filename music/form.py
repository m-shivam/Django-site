from django import forms

class Register(forms.Form):
    uname=forms.CharField(max_length=15)
    uemail=forms.EmailField(max_length=30)
    umob=forms.IntegerField(max_value=9999999999)
    upwd=forms.CharField(forms.PasswordInput())
