from django.shortcuts import render
from twilio.rest import Client
from django.conf import settings
import random
# Create your views here.



def send_verification_call(to, verification_code):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    call = client.calls.create(
        twiml=f'<Response><Say>Your verification code is: {verification_code}</Say></Response>',
        to=to,
        from_=settings.TWILIO_PHONE_NUMBER
    )

    return call.sid

def index(request):
    if request.method == 'POST':
        phone =request.POST.get('phone')
        verification_code = str(random.randint(100000, 999999))
        send_verification_call(phone, verification_code)
        return render(request, 'verification_sent.html')
    
    return render(request, 'index.html')


def verification_sent(request):
    
    return render(request, 'verification_sent.html')
    