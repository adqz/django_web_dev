from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepade(request):
    return HttpResponse('Shits working. <strong> Hurray! </strong>')
