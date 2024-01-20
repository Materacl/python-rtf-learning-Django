from django.shortcuts import render

def demand_page(request):
    return render(request, 'demand.html')
