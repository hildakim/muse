from django.shortcuts import render, redirect, get_object_or_404
import os
import requests
from bs4 import BeautifulSoup
from .models import Review
from .forms import NewReviewForm, ReviewSortForm, AllReviewSortForm
from django.utils import timezone
from django.core.paginator import Paginator
from django.db.models import Q
import datetime
# Create your views here.
from django.contrib.auth.models import User


def index(request):
  page = request.GET.get('page')
  if page is not None:
    showList= showListApi(page)
  else:
    page = "1"
    showList= showListApi(page)
  return render(request, 'reviewindex.html', {'showList':showList, 'page':page})


#choicefield용
# def detail(request, id):
#   mt20id = id
#   showDetail = showDetailApi(mt20id)
#   smallForm = SortSmallForm()
#   newForm = NewReviewForm()
#   if request.method == 'POST': 
#     smallForm = SortSmallForm(request.POST)
#     if smallForm.is_valid():
#       cast = smallForm.cleaned_data['cast']
#       view_date = smallForm.cleaned_data['view_date']
#       view_time = smallForm.cleaned_data['view_time']

#       reviews = Review.objects.filter(mt20id=mt20id)
#       if cast != "":
#         reviews = reviews & Review.objects.filter(Q(cast1__icontains=cast) | Q(cast2__icontains=cast))
#       if view_date != "":
#         view_date = datetime.datetime.strptime(view_date, '%Y-%m-%d')
#         reviews = reviews & Review.objects.filter(view_date = view_date)
#       if view_time != "":
#         view_time = datetime.datetime.strptime(view_time, '%H:%M:%S')
#         reviews = reviews & Review.objects.filter(view_time = view_time)
#       print(reviews)
#   else:
#     reviews = Review.objects.filter(mt20id=mt20id)
#   return render(request, 'showdetail.html', {'showDetail':showDetail, 'newForm':newForm, 'reviews':reviews, 'sortSmallForm':smallForm})


def detail(request, id):
  mt20id = id
  showDetail = showDetailApi(mt20id)
  newForm = NewReviewForm()
  sortForm = ReviewSortForm()
  ratingAvg = ratingAverage(id)
  if request.method == 'POST': 
    sortForm = ReviewSortForm(request.POST)
    if sortForm.is_valid():
      cast = sortForm.cleaned_data['cast']
      view_date = sortForm.cleaned_data['view_date']
      view_time = sortForm.cleaned_data['view_time']
    # cast = request.POST.get('cast')
    # view_date = request.POST.get('date')
    # view_time = request.POST.get('time')

      reviews = Review.objects.filter(mt20id=mt20id)
      if cast != "":
        reviews = reviews & Review.objects.filter(Q(cast1__icontains=cast) | Q(cast2__icontains=cast))
      if view_date != "" and view_date is not None:
        view_date = datetime.datetime.strftime(view_date, '%Y-%m-%d')
        reviews = reviews & Review.objects.filter(view_date = view_date)
      if view_time != "" and view_time is not None:
        view_time = datetime.time.strftime(view_time, '%H:%M')
        reviews = reviews & Review.objects.filter(view_time = view_time)
  else:
    reviews = Review.objects.filter(mt20id=mt20id)
  return render(request, 'showdetail.html', {'showDetail':showDetail, 'newForm':newForm, 'reviews':reviews, 'sortForm':sortForm, 'ratingAvg':ratingAvg})


def showListApi(page):
  open_api_key = os.environ.get('OPEN_API_KEY')
  # cpage = request.GET.get('cpage')
  # stdate = request.GET.get('stdate').replace("-", "")
  # eddate = request.GET.get('eddate').replace("-", "")

  # params = '&rows=5'+'&stdate='+stdate+'&eddate='+eddate+'&cpage='+cpage 
  params = '&stdate=20180101&eddate=20210830&shcate=AAAB&rows=6&cpage='+page
  xmlUrl = 'http://www.kopis.or.kr/openApi/restful/pblprfr?service='+open_api_key+params

  response = requests.get(xmlUrl)
  soup = BeautifulSoup(response.content, 'html.parser')

  data = soup.find_all('db')

  showList = []

  for item in data:
      show = { 'mt20id' : item.find('mt20id').get_text(), 
              'prfnm' : item.find('prfnm').get_text(),
              'prfstate' : item.find('prfstate').get_text(),
              'prfpdfrom' : item.find('prfpdfrom').get_text(),
              'prfpdto' : item.find('prfpdto').get_text(),
              'fcltynm' : item.find('fcltynm').get_text(),
              'poster' : item.find('poster').get_text(),
              'genrenm' : item.find('genrenm').get_text()}
      showList.append(show)
  return showList

def showDetailApi(mt20id):
  open_api_key = os.environ.get('OPEN_API_KEY')
  params = mt20id
  xmlUrl = 'http://www.kopis.or.kr/openApi/restful/pblprfr/'+params+'?service='+open_api_key
  response = requests.get(xmlUrl)
  soup = BeautifulSoup(response.content, 'html.parser')

  data = soup.find_all('db')

  for item in data:
      showDetail = { 'mt20id' : item.find('mt20id').get_text(), 
              'prfnm' : item.find('prfnm').get_text(),
              'prfstate' : item.find('prfstate').get_text(),
              'prfpdfrom' : item.find('prfpdfrom').get_text(),
              'prfpdto' : item.find('prfpdto').get_text(),
              'fcltynm' : item.find('fcltynm').get_text(),
              'poster' : item.find('poster').get_text(),
              'genrenm' : item.find('genrenm').get_text(),
              'prfcast' : item.find('prfcast').get_text(),
              'prfcrew' : item.find('prfcrew').get_text(),
              'prfruntime' : item.find('prfruntime').get_text(),
              'prfage' : item.find('prfage').get_text(),
              'entrpsnm' : item.find('entrpsnm').get_text(),
              'pcseguidance' : item.find('pcseguidance').get_text(),
              'sty' : item.find('sty').get_text(),
              'dtguidance' : item.find('dtguidance').get_text(),
              }
  return showDetail


def new(request, mt20id):
  if request.method == 'POST': 
    form = NewReviewForm(request.POST, request.FILES)
    title = request.POST.get('prfnm')
    if form.is_valid():
      new_review = form.save(commit=False)
      new_review.upload_date = timezone.now()
      new_review.author = request.user
      new_review.mt20id = mt20id
      new_review.title = title
      new_review.save()
      return redirect('review:detail', mt20id)
    return redirect('review:index')


def delete(request, mt20id, id):
  if request.method == 'GET':
    delete_review = Review.objects.get(id = id)
    delete_review.delete()
    return redirect('review:detail', mt20id)

# def allReviews(request):
#   if request.method == 'POST': 
#     sortForm = SortReviewForm(request.POST)

#     if sortForm.is_valid():
#       cast = sortForm.cleaned_data['cast']
#       view_date = sortForm.cleaned_data['view_date']
#       view_time = sortForm.cleaned_data['view_time']
#       title = sortForm.cleaned_data['title']

#       reviewAll = Review.objects.all()
#       if title != "":
#         reviewAll = Review.objects.filter(title = title)
#       if cast != "":
#         reviewAll = reviewAll & Review.objects.filter(Q(cast1__icontains=cast) | Q(cast2__icontains=cast))
#       if view_date != "":
#         view_date = datetime.datetime.strptime(view_date, '%Y-%m-%d')
#         reviewAll = reviewAll & Review.objects.filter(view_date = view_date)
#       if view_time != "":
#         view_time = datetime.datetime.strptime(view_time, '%H:%M:%S')
#         reviewAll = reviewAll & Review.objects.filter(view_time = view_time)

#   else:
#     reviewAll = Review.objects.all()
#     sortForm = SortReviewForm()
#   return render(request, 'allreviews.html', {'reviewAll':reviewAll, 'sortForm':sortForm})


def allReviews(request):
  allSortForm = AllReviewSortForm()
  if request.method == 'POST':
    # title = request.POST.get('title')
    # cast = request.POST.get('cast')
    # view_date = request.POST.get('date')
    # view_time = request.POST.get('time')
    allSortForm = AllReviewSortForm(request.POST)
    if allSortForm.is_valid():
      cast = allSortForm.cleaned_data['cast']
      view_date = allSortForm.cleaned_data['view_date']
      view_time = allSortForm.cleaned_data['view_time']
      title = allSortForm.cleaned_data['title']

      reviewAll = Review.objects.all()
      if title != "":
        reviewAll = Review.objects.filter(Q(title__icontains=title))
      if cast != "":
        reviewAll = reviewAll & Review.objects.filter(Q(cast1__icontains=cast) | Q(cast2__icontains=cast))
      if view_date != ""and view_date is not None:
        view_date = datetime.datetime.strftime(view_date, '%Y-%m-%d')
        reviewAll = reviewAll & Review.objects.filter(view_date = view_date)
      if view_time != ""and view_time is not None:
        view_time = datetime.time.strftime(view_time, '%H:%M')
        reviewAll = reviewAll & Review.objects.filter(view_time = view_time)
    
  else:
    reviewAll = Review.objects.all()
  return render(request, 'allreviews.html', {'reviewAll':reviewAll, 'allSortForm': allSortForm})

def showSearch(request):
  page = request.GET.get('page')
  title = request.GET.get('title')
  # print('검색어', title)
  if page is not None:
    showList= showSearchApi(title, page)
  else:
    page = "1"
    showList= showSearchApi(title, page)
  return render(request, 'reviewindex.html', {'showList':showList, 'page':page, 'title': title})


def showSearchApi(title, page):
  # shprfnm
  open_api_key = os.environ.get('OPEN_API_KEY')
  # cpage = request.GET.get('cpage')
  # stdate = request.GET.get('stdate').replace("-", "")
  # eddate = request.GET.get('eddate').replace("-", "")

  # params = '&rows=5'+'&stdate='+stdate+'&eddate='+eddate+'&cpage='+cpage 
  params = '&stdate=20180101&eddate=20210830&rows=6&shcate=AAAB&cpage='+page+"&shprfnm="+title
  xmlUrl = 'http://www.kopis.or.kr/openApi/restful/pblprfr?service='+open_api_key+params

  response = requests.get(xmlUrl)
  soup = BeautifulSoup(response.content, 'html.parser')

  data = soup.find_all('db')

  showList = []

  for item in data:
      show = { 'mt20id' : item.find('mt20id').get_text(), 
              'prfnm' : item.find('prfnm').get_text(),
              'prfstate' : item.find('prfstate').get_text(),
              'prfpdfrom' : item.find('prfpdfrom').get_text(),
              'prfpdto' : item.find('prfpdto').get_text(),
              'fcltynm' : item.find('fcltynm').get_text(),
              'poster' : item.find('poster').get_text(),
              'genrenm' : item.find('genrenm').get_text()}
      showList.append(show)
  return showList


def ratingAverage(mt20id):
  rating_qs = Review.objects.filter(mt20id=mt20id).values('rating')
  sum = 0
  for i in rating_qs:
    sum += i.get('rating')

  if sum != 0:
    avg = sum / rating_qs.count()
    avg = round(avg, 2)
  else:
    avg = 0
  print(sum,rating_qs.count(),avg)
  return avg