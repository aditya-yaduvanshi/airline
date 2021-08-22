from django.shortcuts import render, reverse
from .models import *
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
    return render(request, "flights/index.html",{
        "flights" : Flight.objects.all()
    })

def flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    passengers = flight.passengers.all()
    nonpassengers = Passenger.objects.exclude(flights=flight).all()
    return render(request, "flights/flight.html",{
        "flight" : flight,
        "passengers" : passengers,
        "nonpassengers" : nonpassengers
    })

def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passengerid = int(request.POST["passenger"])
        passenger = Passenger.objects.get(pk=passengerid)
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=(flight_id,)))
