from django.shortcuts import render
from . models import *
# Create your views here.
def home(request):
    ct=categ.objects.all()
    prod = products.objects.all()
    return render(request,'index.html',{'pr':prod,'ct':ct})