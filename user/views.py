from django.shortcuts import render , redirect
from .forms import Userregister
# from django.contrib import messages

# Create your views here.
def create_user(request):
    if request.method == 'POST':
        form = Userregister(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request,'account created sucessfully')
            return redirect('register')
    else:
        form = Userregister()
    return render(request, 'register.html',{'form':form})
