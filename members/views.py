from django.shortcuts import render
from django.http import HttpResponse
from Model import *

def index(request):
    symptoms=request.GET.get("symptoms")
    response =predictDisease(symptoms)

    return HttpResponse(response)