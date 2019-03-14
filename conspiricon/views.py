from django.shortcuts import render, redirect

from .forms import PresentationForm, RSVPForm
from .models import Presentation, RSVP


def index(request):
    context = {}
    return render(request, 'index.html', context)

def faq(request):
    context = {}
    return render(request, 'faq.html', context)


def rsvp(request):
    form = RSVPForm()
    attendees = RSVP.objects.all()
    context = {'form': form, 'attendees': attendees}
    return render(request, 'rsvp.html', context)

def submit_rsvp(request):
    if request.method == 'POST':
        form = RSVPForm(request.POST)
        if form.is_valid():
            form.save()        
    return redirect('rsvp')

def presentations(request):
    form = PresentationForm()
    presentations = Presentation.objects.all()
    context = {'form': form, 'presentations': presentations}
    return render(request, 'presentations.html', context)

def submit(request):
    if request.method == 'POST':
        form = PresentationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    return redirect('presentations')
