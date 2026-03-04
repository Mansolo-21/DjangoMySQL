from django.shortcuts import render, redirect
from .forms import ProductForm


def index(request):
    form = ProductForm()
    return render(request, 'index.html',{'form':form})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  
            return redirect('index') 
        else:
            print(form.errors)  
    else:
        form = ProductForm()
    return render(request, 'addproduct.html', {"form": form})
