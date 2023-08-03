from django.shortcuts import render,HttpResponse
from .models import Contact

# Create your views here.
def index(requets):
    if requets.method == 'POST':
        name = requets.POST['name']
        email = requets.POST['email']
        subject = requets.POST['subject']
        message = requets.POST['message']
        contact = Contact(name =name , email = email, subject = subject, message= message)
        contact.save()
    return render(requets,"index.html")

def cars(requets):
    return render(requets,"cars.html")

def contact(requets):
    return render(requets,"contact.html")

def about(requets):
    return render(requets,"about.html")

def terms(requets):
    return render(requets,"terms.html")

def faq(requets):
    return render(requets,"faq.html")