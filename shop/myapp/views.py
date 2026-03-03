from django.shortcuts import render, redirect
from .forms import ProductForm


def index(request):
    form = ProductForm()
    return render(request, 'index.html',{'form':form})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # ✅ save to DB
            return redirect('index')  # ✅ redirect after save
        else:
            print(form.errors)  # ✅ print errors if invalid
    else:
        form = ProductForm()
    return render(request, 'index.html', {"form": form})
