from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User

# Create your views here.


def login1(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        
        print(username)
        print(password)
        print(user)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            mass='invalid username and password'
            return render(request, 'login2.html', {'mass':mass})
            

    else:
        return render(request, 'login2.html')


def register(request):

   

    if request.method=='POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        password1 = request.POST['password1']
        
        email = request.POST['email']
                  

        if password==password1:
           
            pmsg=""
            mm=""
            
          
            if User.objects.filter(username=username).exists():
                umsg='The username was Teken'
                mm='m1'
                return render(request, 'Register1.html',{'umsg':umsg, 'mm':mm})

                                                                                                                                                                                                                                                                                                    
                  
            elif  User.objects.filter(email=email).exists(): 
                
                emsg='The email was Teken'
                mm='m1'
                return render(request, 'Register1.html',{'emsg':emsg, 'm2':mm})   

            else:
                
                user= User.objects.create_user(username=username , first_name=first_name, email=email, password=password, last_name=last_name)
                user.save();
                umsg=""
                emsg=""
                
                print('content saved')
                auth.login(request, user)
                return redirect('/')
                
        else:
            passmsg='The password was Not Mach'
            mm='m1'
            

         
            
            return render(request, 'Register1.html', {'passmsg':passmsg, 'm3':mm} )
            
        
    else:
        return render(request, 'Register1.html')

def logout(request):
    auth.logout(request)
    return redirect('/')