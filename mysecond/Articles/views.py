from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index (request):
    return HttpResponse("Hello, people! If this shit works, I will continue study this bullshit")