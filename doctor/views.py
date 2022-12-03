from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def doctor_view(*args, **kwargs):
    return HttpResponse("<h1>Doctor Page will be here!</h1>")
