from django.shortcuts import render

# Create your views here.

def cult(request):
    return render(request, "cult_page.html")
