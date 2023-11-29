from django.shortcuts import render

def index(request):
    return render(request,'home.html')

def about(request):
    return render(request,'aboutus.html')

def userinput(request):
    return render(request,'userinput.html')

def viewdata(request):
    email = request.GET.get('email', '')  # Use get to avoid KeyError if 'email' is not present
    password = request.GET.get('Pass', '')  # Use get to avoid KeyError if 'Pass' is not present

    data = {
        'email': email,  # Correct variable name
        'password': password,  # Correct variable name
    }

    return render(request, 'viewdata.html', data)

