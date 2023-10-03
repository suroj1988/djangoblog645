from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def index(request):
    views = {}
    views['services'] = Service.objects.all()
    views['feedbacks'] = Feedback.objects.all()
    return render(request,'index.html',views)

def about(request):
    views = {}
    views['feedbacks'] = Feedback.objects.all()
    return render(request,'about.html',views)

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        data = Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )
        data.save()
        return redirect('/contact')
    return render(request, 'contact.html')

