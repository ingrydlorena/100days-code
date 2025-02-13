from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    text ='''
    Hello world!
    Welcome to challenge day 63 of python :D
    '''
    return HttpResponse(text)

