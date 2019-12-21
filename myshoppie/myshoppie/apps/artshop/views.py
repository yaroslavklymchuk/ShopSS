from django.shortcuts import render

# Create your views here.

def ResponseForArtshop(request):
   return render(request, "Home _ BONA FIDES.html")

def ResponseForBucket(request):
   return render(request, "Корзина | BONA FIDES.html")