from django.urls import path
import payment.views as v

urlpatterns = [path("", v.index), path("payment/", v.payment)]
