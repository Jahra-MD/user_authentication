from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def IndexView(request):
    return render(request,'index.html')
    
@login_required
def dashboardView(request):
    return render(request,'dashboard.html')


def registerView(request):
    if request.method=="POST":
        form =UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form =UserCreationForm()


    return render(request,'registration/register.html',{'form':form})