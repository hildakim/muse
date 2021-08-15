from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['receiver','title','body']


class StaticReceiverForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['title','body']