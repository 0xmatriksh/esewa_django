from django.shortcuts import render

import uuid


# Create your views here.
def index(request):

    # generate random code for transaction UUID
    random_code = uuid.uuid4()

    context = {"transaction_code": random_code}
    return render(request, "payment/index.html", context=context)
