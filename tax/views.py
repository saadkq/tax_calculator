from django.http import HttpResponse
from django.shortcuts import render

tax_rate = 15

def default(request):
    return HttpResponse("<h1>This is a site to calculate tax</h1>")

def calculate_price(request, num):
    
    num = int(num)
    
    total_price = num + (num * tax_rate / 100)
    return HttpResponse("<h1>Total price after tax: {}</h1>".format(total_price))

def show_tax_rate(request):
    return render(request, 'taxrate.html', {'tax_rate': tax_rate})
