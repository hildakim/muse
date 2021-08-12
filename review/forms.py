from django import forms
from django.forms import Form, CharField, TextInput, PasswordInput, ChoiceField, BooleanField
from django.forms import widgets
from django.forms.fields import DateField, DateTimeField, ImageField, IntegerField, SplitDateTimeField, TimeField
from django.forms.widgets import DateTimeInput, NumberInput, Textarea
from django.utils.regex_helper import Choice
from .models import Review


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


# class SortReviewForm(forms.ModelForm):
#     SortCondition.TITLE_CHOICES.insert(0, ('', '---------'))
#     SortCondition.CAST_CHOICES.insert(0, ('', '---------'))
#     SortCondition.DATE_CHOICES.insert(0, ('', '---------'))
#     SortCondition.TIME_CHOICES.insert(0, ('', '---------'))
#     title = ChoiceField(label="공연명", choices=SortCondition.TITLE_CHOICES, required=False)
#     cast = ChoiceField(label="배우", choices=SortCondition.CAST_CHOICES, required=False)
#     view_date = ChoiceField(label="관람일", choices=SortCondition.DATE_CHOICES, required=False)
#     view_time = ChoiceField(label="관람시간", choices=SortCondition.TIME_CHOICES, required=False)
#     class Meta:
#         model = SortCondition
#         fields = ['title', 'title2', 'cast', 'view_date', 'view_time']


# class SortSmallForm(forms.ModelForm):
#     cast = ChoiceField(label="배우", choices=SortCondition.CAST_CHOICES, required=False)
#     view_date = ChoiceField(label="관람일", choices=SortCondition.DATE_CHOICES, required=False)
#     view_time = ChoiceField(label="관람시간", choices=SortCondition.TIME_CHOICES, required=False)
#     class Meta:
#         model = SortCondition
#         fields = [ 'cast', 'view_date', 'view_time']


class ReviewSortForm(Form):
    cast = CharField(
        widget = TextInput( attrs={'placeholder': '배우 이름'}),
        label='배우',
        required=False
    )
    view_date = DateField( 
        widget = DateInput(),
        label='관람일', 
        required=False
    )
    view_time = TimeField(
        widget = TimeInput(),
        label='관람시간',
        required=False
    )
    

class AllReviewSortForm(Form):
    title = CharField(
        widget = TextInput( attrs={'placeholder': '제목'}),
        label='제목',
        required=False
    )
    cast = CharField(
        widget = TextInput( attrs={'placeholder': '배우 이름'}),
        label='배우',
        required=False
    )
    view_date = DateField( 
        widget = DateInput(),
        label='관람일', 
        required=False
    )
    view_time = TimeField(
        widget = TimeInput(),
        label='관람시간',
        required=False
    )