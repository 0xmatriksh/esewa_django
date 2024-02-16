from django.shortcuts import render

import uuid
import requests

ESEWA_PAYMENT_URL = "https://epay.esewa.com.np/api/epay/main/v2/form"
PRODUCT_CODE = "EPAYTEST"
FAILURE_URL = "https://google.com"
SUCESS_URL = "https://esewa.com.np"

from payment.utils import generate_signature


# Create your views here.
def index(request):

    # generate random code for transaction UUID
    random_code = uuid.uuid4()

    context = {"transaction_code": random_code}
    return render(request, "payment/index.html", context=context)


def payment(request):
    service_charge = 0
    delivery_charge = 0
    if request.method == "POST":
        random_code = uuid.uuid4()
        amount = request.POST.get("amount")
        tax_amount = request.POST.get("tax_amount")
        total_amount = int(amount) + int(tax_amount) + service_charge + delivery_charge

        message = f"total_amount={total_amount},transaction_uuid=${random_code},product_code=${PRODUCT_CODE}"
        signed_field_names = "total_amount,transaction_uuid,product_code"

        signature = generate_signature(message)

        esewa_pay_formdata = {
            "amount": amount,
            "failure_url": FAILURE_URL,
            "product_delivery_charge": delivery_charge,
            "product_service_charge": service_charge,
            "product_code": PRODUCT_CODE,
            "signature": signature,
            "signed_field_names": signed_field_names,
            "success_url": SUCESS_URL,
            "tax_amount": tax_amount,
            "total_amount": str(total_amount),
            "transaction_uuid": random_code,
            "esewa_url": ESEWA_PAYMENT_URL,
        }

        print(esewa_pay_formdata)

        return render(
            request,
            "payment/pay.html",
            context=esewa_pay_formdata,
        )

    context = {
        "service_charge": service_charge,
        "delivery_charge": delivery_charge,
    }

    return render(request, "payment/payment.html", context=context)
