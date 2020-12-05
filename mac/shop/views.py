from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def request(index):
    return HttpResponse("Index Shop")