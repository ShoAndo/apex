from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
# Create your views here.

def index(request):
  return 'Hello World'