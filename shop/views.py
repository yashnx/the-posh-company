from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact
from math import ceil

def index(request):
    products= Product.objects.all()
    n= len(products)
    nRow= n//3+ceil((n/3)-(n//3))
    params = {'no_of_rows':nRow, 'range': range(1,nRow),'product': products}
    return render(request, 'shop/index.html',params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    if request.method=="POST":
        print(request)
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        phone=request.POST.get('phone', '')
        desc=request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')

def search(request):
    return HttpResponse("we are at search")

def productview(request):
    return HttpResponse("we are at product view")

def cart(request):
    return render(request, 'shop/cart.html')


# Create your views here.
