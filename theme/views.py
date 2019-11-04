from test1.settings import BASE_DIR
from django.shortcuts import render

def index(request):
    return render(request, "index.html")



# Create your views here.
