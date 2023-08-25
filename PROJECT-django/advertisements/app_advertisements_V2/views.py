from django.shortcuts import render

def index(request):
    return render(request,"index.html")
    # return HttpResponce()

def top_sellers(request):
    return render(request, "top-sellers.html")
