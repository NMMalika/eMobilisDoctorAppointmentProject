from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.
def home(request):
    return render(request, "index.html")
def about(request):
    return render(request, "about.html")
def appointment(request):
    if request.method == "POST":
        name = request.POST["your_name"]
        email = request.POST["your_email"]
    

        return render(request, "contact.html",
                      {"your_name": your_name, "your_email": your_email, "subject": subject, "message": message})

    else:

       return render(request, "appointment.html")


def contact(request):
    if request.method == "POST":
        your_name = request.POST["your_name"]
        your_email = request.POST["your_email"]
        subject = request.POST["subject"]
        message = request.POST["message"]

        return render(request, "contact.html", {"your_name": your_name, "your_email": your_email, "subject": subject, "message": message})

    else:
          return render(request, "contact.html")



def price(request):
    return render(request, "price.html")


def search(request):
    return render(request, "search.html")


def service(request):
    return render(request, "service.html")


def team(request):
    return render(request, "team.html")


def testimonial(request):
    return render(request, "testimonial.html")


def blog(request):
    return render(request, "blog.html")