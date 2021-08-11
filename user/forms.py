from allauth.account.forms import SignupForm
from django.contrib.auth.forms import UserChangeForm
from django import forms
from .models import CustomUser

class CustomSignupForm(SignupForm):
    nickname = forms.CharField(label='닉네임', widget=forms.TextInput(attrs={'placeholder': '익명의사자'}))
    birth = forms.DateField(label='생년월일', widget=forms.DateInput(attrs={'placeholder': '1900-01-01'}))

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.nickname = self.cleaned_data['nickname']
        user.birth = self.cleaned_data['birth']
        user.save()
        return user

class CustomCsUserChangeForm(UserChangeForm):
    password = None        
    username = forms.CharField(label='아이디', widget=forms.TextInput(attrs={'readonly':'readonly'}))
    nickname = forms.CharField(label='닉네임')
    birth = forms.DateField(label='생년월일')

    class Meta:
        model = CustomUser
        fields = ['username', 'nickname', 'birth']