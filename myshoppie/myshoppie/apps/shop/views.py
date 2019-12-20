from django.shortcuts import render


def ShopResponse(request):
	return render(request, "index.html")

