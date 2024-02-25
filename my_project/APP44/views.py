from django.shortcuts import render
from django.http import HttpResponse

def default(request)
    return render(request, 'APP44/default.html')

def calculate_tax(request, any_number):
    tax_rate = 0.15
    price = float(any_number)
    total = price + (price * tax_rate)
    return HttpResponse(f'Total price with 15% tax: {total}')
def tax_rate_view(request):
    tax_rate = 0.15
    return render(request, 'APP44/taxRate.html', {'tax_rate': tax_rate})

