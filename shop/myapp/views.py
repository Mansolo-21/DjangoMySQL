from django.shortcuts import render,redirect
from django_daraja.mpesa.core import MpesaClient
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .forms import ProductForm
# Create your views here.
def index(request):
    return render(request,'index.html')

def add_product(request):
    if request.method == 'POST':
        form=ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=ProductForm()
    return render(request,'addproduct.html',{'form':form})




def lipa_na_mpesa(request):
    if request.method == 'POST':
        phone_number = request.POST.get("phone")
        amount = int(request.POST.get("amount"))
        if not phone_number or not amount:
            return HttpResponse("Phone or amount missing")

        try:
            amount = int(amount)
        except ValueError:
            return HttpResponse("Invalid amount")

        account_reference = "firefox"
        transaction_desc = "payment of school fees"
        callback_url = "https://alleen-nardine-adena.ngrok-free.dev/callback/"
        
        cl = MpesaClient()
        response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)

        return HttpResponse(f"Payment request sent. Response: {response}")

    # If GET request, show the form
    return render(request, 'pay.html')

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        data = json.loads(request.body)  # parse JSON payload
        print("M-Pesa callback data:", json.dumps(data, indent=2))
        # You can update your database here with transaction info
        return JsonResponse({"status": "success"})
    return JsonResponse({"status": "Invalid request"})
