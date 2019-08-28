from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="用户名")
    password = forms.CharField(widget=forms.PasswordInput,min_length=8,label="密码")


