from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import PhoneCatalog

def index(request):
    message = None
    if "message" in request.GET:
        message = request.GET["message"]
    
    return render(request, "index.html", {
        "phones":
            PhoneCatalog.objects.order_by('-reg_date')[:5],
        "message": message
    })


def phone(request, phone_id):
    error_message = None
    if "error_message" in request.GET:
        error_message = request.GET["error_message"]
    return render(request, "phone.html", {
        "phone": get_object_or_404(PhoneCatalog, pk=phone_id),
        "error_message": error_message
    })