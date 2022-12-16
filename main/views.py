from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import get_user_model
# Create your views here.
#Email sending 
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

User = get_user_model()

def home(response):
    return HttpResponse("Home Page")
    
def register(request):

    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save() 
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("register_user/")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request, template_name="main/register.html", context={"register_form":form})

def users(request):
    users = User.objects.all()

    return render(request, "main/users.html", {"users" : users})

def delete_user(request, id):
    user = User.objects.get(id=id)
    if id is not None:
        user.delete()
    users = User.objects.all()

    return render(request, "main/users.html", {"users" : users})

def send_email_to(request):
    email = EmailMessage(
        'Test Email' ,
        'Hello there, I am testing out this email. Nice day',
        'noreply@kampalapolytechnicmengo.ac.ug', 
        ['fredowampz@gmail.com',
        ]
    ).send()

    return HttpResponse("<h1>Email has been sent successfully<h1>")
# def edit_user(request, id):
    
#     if id is not None:
#         user = User.objects.get(id=id)
#     if request.Method == "POST":
#         if id is not None:
#             user = User.objects.get(id=id)
#             user.save()

#     return render(request, "main/users.html", {"users" : users})