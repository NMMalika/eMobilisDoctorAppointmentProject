from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "index.html")
def about(request):
    return render(request, "about.html")
def appointment(request):
    return render(request, "appointment.html")


def contact(request):
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