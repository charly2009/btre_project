from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import state_choices, price_choices, bedroom_choices
# Create your views here.
def index (request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    contex = {
        'listings': listings,
        'bedroom_choices' : bedroom_choices,
        'state_choices': state_choices,
        'price_choices': price_choices,
    }
    return render (request, 'pages/index.html', contex)

def about (request):
    #GET ALL REALTORS
    realtors = Realtor.objects.order_by('-hire_date')

    #GET MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    contex = {
        'realtors' : realtors,
        'mvp_realtors' : mvp_realtors
    }

    return render (request, 'pages/about.html', contex)