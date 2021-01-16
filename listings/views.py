from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger
from .choices import state_choices, price_choices, bedroom_choices
from realtors.models import Realtor
#from django.shortcuts import get_object_or_404
#from django.http import HttpResponse
from .models import Listing
# Create your views here.
def index (request):
    listings =  Listing.objects.order_by('-list_date').filter(is_published = True) # to grab object objects from a model created before
    #list according the publish date
    #filter only published artticles by adding this condition only articles checked published in admin area will be showwn
    #Listing.object.all()
    paginator = Paginator(listings, 3) #load 3 items
    page = request.GET.get('page')
    page_listings = paginator.get_page(page)
    contex= {
        'listings' : page_listings
    }
    return render (request, 'listings/listings.html', contex)

def listing (request, listing_id):

    listing = get_object_or_404 (Listing, pk= listing_id)
    contex = {
        'listing': listing,
    }

    return render (request, 'listings/listing.html', contex)

def search (request):
    # Get initial selection sorted by date
    queryset_list = Listing.objects.order_by('-list_date')

    # Filter by contains Keywords
    # check if the keyword exist
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)# check if the key word is in the description

    # Filter by exact city
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # Filter by exact state
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state) # with iexact = the word must be in low characeter

    # Filter by max bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    # Filter by max price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)