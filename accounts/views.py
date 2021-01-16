from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from contacts.models import Contact
# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user= auth.authenticate(username = username , password = password)
        if user is not None: # IF THE USER IS ALREADY REGISTERED SO IT IS IN DATABASE
            auth.login(request , user)
            messages.success(request ,  'You are now logged ')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials ')
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        ## register user

        if password == password2:
            #check username
            if User.objects.filter(username = username).exists():
                messages.error(request, 'this username is taken ')
                return redirect('register')
            else:
                if User.objects.filter(email = email).exists():
                    messages.error(request, 'that email has been used ')
                    return redirect('register')
                #else create it
                else:
                    # after creating a profile you can be able to login
                    user = User.objects.create_user(username = username , password= password, email= email ,
                                                    first_name = first_name , last_name =  last_name )
                    #login after register
                    # after register you logged automatically and it bring you to homepage
                    #auth.login(request , user )
                    #messages.success(request, 'You are now logged in ')
                    #return redirect('index ') # after register you logged and it bring you to homepage
                    user.save()
                    messages.success(request, 'You are now registered and can log in ')
                    return redirect('login') # it will display login page so you can login it with


        # show this error
        else:
            messages.error(request, 'password does not match ')
            return redirect('register')

    else:
        return render (request, 'accounts/register.html')

def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id = request.user.id)
    contex = {
        'contacts': user_contacts
    }
    return render (request, 'accounts/dashboard.html' , contex )

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request , 'You have successfuly logged out ')
        return redirect ('index')