from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

def register(request):
    if(request.method=='POST'): #after data added in the form 
        name = request.POST['name']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        if(pass1==pass2):
            if(User.objects.filter(username=name).exists()):
                messages.info(request,'user name exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=name,email=email,password=pass1)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'password miss match')
            return redirect('register')
            
    return render(request,"register.html") #in nav bar just call the register.html which is GET
def login(request):
    if(request.method=='POST'):
        name = request.POST['name']
        pass1 = request.POST['password1']
        user = auth.authenticate(username=name,password=pass1)
        if(user is None):
            messages.info(request,"invalid username")
            return redirect('login')
        auth.login(request,user)
        return redirect("/")
    
    return render(request,"login.html") 
def logout(request):
    auth.logout(request)
    return redirect("/")