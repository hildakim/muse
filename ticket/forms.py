from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['ticket','contents','image']

        widgets = {
            'contents': forms.Textarea(
            attrs={'placeholder': '티켓은 원가 양도만 가능합니다. 원가 양도를 제외한 양도는 불법입니다.'}),
        }