from django.core.checks import messages
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import EmailMessage, send_mail, message
from django.conf import settings
from django.contrib import messages

from board.models import Doctor


# Create your views here.
def home(request):
    return render(request, "index.html")
def about(request):
    return render(request, "about.html")
def appointment(request):

    doctor = Doctor.objects.all()
    if request.method == "POST":
        department = request.POST["department"]
        doctor = request.POST["doctor"]
        name = request.POST["name"]
        email = request.POST["email"]
        date = request.POST["date"]
        time = request.POST["time"]

        messages.add_message(request, messages.SUCCESS,f"{message}")
    else:

         return render(request, "appointment.html",{"doctor":doctor})


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