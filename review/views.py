from django.shortcuts import render, redirect, get_object_or_404
import os
import requests
from bs4 import BeautifulSoup
from .models import Review
from .forms import NewReviewForm, SortReviewForm
from django.utils import timezone
from django.core.paginator import Paginator
from django.db.models import Q
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

def detail(request, id):
  mt20id = id
  showDetail = showDetailApi(mt20id)
  reviews = Review.objects.filter(mt20id=mt20id)
  newForm = NewReviewForm()
  return render(request, 'showdetail.html', {'showDetail':showDetail, 'newForm':newForm, 'reviews':reviews})


def showListApi(page):
  open_api_key = os.environ.get('OPEN_API_KEY')
  # cpage = request.GET.get('cpage')
  # stdate = request.GET.get('stdate').replace("-", "")
  # eddate = request.GET.get('eddate').replace("-", "")

  # params = '&rows=5'+'&stdate='+stdate+'&eddate='+eddate+'&cpage='+cpage 
  params = '&stdate=20200601&eddate=20210630&rows=5&cpage='+page
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
      # new_review.author = request.user
      new_review.author = User.objects.get(username='hilda')
      new_review.mt20id = mt20id
      new_review.title = title
      new_review.save()
      return redirect('review:detail', mt20id)
    return redirect('review:index')

def allReviews(request):
  reviewAll = Review.objects.all()
  if request.method == 'POST': 
    sortForm = SortReviewForm(request.POST)
    # reviewAll = Review.objects.filter(view_date = request.POST.get('view_date').view_date)
  else:
    sortForm = SortReviewForm()
  return render(request, 'allreviews.html', {'reviewAll':reviewAll, 'sortForm':sortForm})


