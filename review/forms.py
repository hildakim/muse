from django import forms
from django.forms import Form, CharField, TextInput, PasswordInput, ChoiceField, BooleanField
from django.forms import widgets
from django.forms.fields import DateField, DateTimeField, ImageField, IntegerField, SplitDateTimeField, TimeField
from django.forms.widgets import DateTimeInput, NumberInput, Textarea
from .models import Review

# class ReviewForm(forms.ModelForm):
#     class Meta:
#         model = Review
#         fields = ['rating', 'view_date', 'view_time', 'cast1', 'cast2', 'body', 'image']

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class NewReviewForm(forms.ModelForm):
    rating = IntegerField(
        widget = NumberInput(attrs = { 'max':10, 'step':1, 'min':0 }),
        label='만족도'
    )
    view_date = DateField( 
        widget = DateInput(),
        label='관람일'
    )
    view_time = TimeField(
        widget = TimeInput(),
        label='관람시간'
    )
    cast1 = CharField(
        widget = TextInput( attrs={'placeholder': '배우명'}),
        label='출연 배우(1)'
    )
    cast2 = CharField(
        widget = TextInput( attrs={'placeholder': '배우명'}),
        required=False,
        label='출연 배우(2)'
    )
    body = CharField(
        widget = Textarea(attrs={'placeholder': '후기를 작성해주세요'}),
        label = "후기"
    )
    image = ImageField(required=False, label='사진 첨부')
    class Meta:
        model = Review
        fields = ['rating', 'view_date','view_time', 'cast1', 'cast2', 'body', 'image']