from django.shortcuts import render
from .forms import SignupForm
from django.views.generic import CreateView, View, TemplateView
from .models import Signup, Price
from django.shortcuts import redirect, HttpResponseRedirect, reverse

from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

# find the term, and relevant info depending on which school is chosen

"""
class CreateCheckoutSessionView(View):
    print("It has redirected to CreateCheckoutSessionView")
    def post(self, request, *args, **kwargs):
        price = Price.objects.get(id=self.kwargs["pk"])
        domain = "https://yourdomain.com"
        if settings.DEBUG:
            domain = "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': price.stripe_price_id, #price_1NSysSDLyQxfo6M0MdfpQROa
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=domain + '/success/',
            cancel_url=domain + '/cancel/',
        )
        return redirect(checkout_session.url)


def SignupView(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = SignupForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()

            #return HttpResponseRedirect("success.html")
            
            return HttpResponseRedirect(reverse('create-checkout-session', args=[2]))

            #context = {
            #    "child": form.cleaned_data['child_name'],
            #    "school": form.cleaned_data['school'],
            #}
            

    else:
    	form = SignupForm()

    return render(request, "signup/signup_form.html", {"form": form})
"""

def SignupView(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = SignupForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()

            price = Price.objects.get(pk=1)#id=kwargs["pk"])
            domain = "http://127.0.0.1:8000"

            if settings.DEBUG:
                domain = "http://127.0.0.1:8000"
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                {
                    'price': price.stripe_price_id,
                    'quantity': 1,
                },
                ],

                mode = 'payment',
                success_url=domain+'/signedup/',
                cancel_url=domain+'/cancel/'
            )
            return redirect(checkout_session.url)

    else:
        form = SignupForm()

    return render(request, "signup/signup_form.html", {"form": form})


class SuccessView(TemplateView):
    template_name = "signup/reg_success.html"


class CancelView(TemplateView):
    template_name = "signup/cancel.html"