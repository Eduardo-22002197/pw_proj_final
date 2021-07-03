import proj2
from django.shortcuts import render

# Create your views here.
def home_page_view(request):
    return render(request, 'proj2/index.html')

def history_page_view(request):
    return render(request, 'proj2/history.html')

def location_page_view(request):
    return render(request, 'proj2/location.html')

def contact_page_view(request):
    return render(request, 'proj2/contact.html')

def about_page_view(request):
    return render(request, 'proj2/about.html')
