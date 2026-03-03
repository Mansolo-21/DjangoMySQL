from django.shortcuts import render,redirect
from  .forms import ProductForm
# Create your views here.
def index(request):
    return render(request,'index.html')

def add_product(request):
  if request.method =='POST':
    form= ProductForm()
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request,'index.html') 