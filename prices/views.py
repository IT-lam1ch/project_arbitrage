from django.shortcuts import render
from .utils import fetch_prices

def compare_prices(request):
    comparisons = fetch_prices(limit=100)
    return render(request, "compare_prices.html", {"comparisons": comparisons})
