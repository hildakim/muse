from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Ticket
from .forms import TicketForm

# Create your views here.

def ticket(request):
    contents = Ticket.objects.all()
    ticket_list = Ticket.objects.all().order_by('-id')
    paginator = Paginator(ticket_list, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'ticket_home.html', {'contents': contents, 'posts':posts})


def detail(request, id):
    data = get_object_or_404(Ticket, pk = id)
    return render(request, 'ticket_detail.html', {'data':data})

def new(request):
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, request.FILES)
        if ticket_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.date = timezone.now() #날짜 생성
            ticket.author = request.user
            ticket.save()
            return redirect('ticket:ticket')
    else:
        ticket_form = TicketForm()
        return render(request, 'ticket_new.html', {'form':ticket_form})

def edit(request, id):
    post = get_object_or_404(Ticket, pk = id)
    if request.method == 'GET':
        ticket_form = TicketForm(instance = post)
        return render(request, 'ticket_edit.html', {'edit_ticket' : ticket_form, 'ticket' : post})
    else:
        ticket_form = TicketForm(request.POST, request.FILES, instance = post)
        if ticket_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.date = timezone.now() 
            ticket.save()
        return redirect('ticket:ticket_detail', ticket.id)

def delete(request, id):
    erase_ticket = Ticket.objects.get(id = id)
    if request.user == erase_ticket.author:
        erase_ticket.delete()
    return redirect('ticket:ticket')

def messenger(request, id):
    post = get_object_or_404(Ticket, pk = id)
    if request.method == 'GET':
        ticket_form = TicketForm(instance = post)
        return render(request, 'ticket_edit.html', {'edit_ticket' : ticket_form})
    else:
        ticket_form = TicketForm(request.POST, request.FILES, instance = post)
        if ticket_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.date = timezone.now() 
            ticket.save()
        return redirect('ticket:ticket_detail', ticket.id)

def search(request):
    tickets = Ticket.objects.all().order_by('-id')
    q = request.POST.get('q', "") 

    if q:
        tickets = tickets.filter(ticket__icontains=q) | tickets.filter(contents__icontains=q)
        return render(request, 'search.html', {'tickets' : tickets, 'q' : q})
    else:
        return render(request, 'search.html')