from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.http import JsonResponse
from dotenv import load_dotenv
import os

load_dotenv()
# Create your views here.
def home(request):
    return JsonResponse({'page':"ITSA"},safe=True)

    # return 

def login(request):
    sid = request.POST['sid']
    password = request.POST['password']

    pass

def signup(request):
    sid = request.POST['sid']
    name = request.POST['name']
    email = request.POST['email']
    pass