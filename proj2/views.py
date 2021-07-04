import proj2
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Contact
from .forms import CommentForm, ContactForm

# Create your views here.
def home_page_view(request):
    return render(request, 'proj2/index.html')

def history_page_view(request):
    return render(request, 'proj2/history.html')

def location_page_view(request):
    return render(request, 'proj2/location.html')

def contact_page_view(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('proj2:contact'))

    context = {'form': form}
    return render(request, 'proj2/contact.html', context)

def comments_page_view(request):
    form = CommentForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('proj2:comments'))

    context = {'form': form}
    return render(request, 'proj2/comments.html', context)

def quiz_page_view(request):
    return render(request, "proj2/quiz.html")

def about_page_view(request):
    return render(request, 'proj2/about.html')
