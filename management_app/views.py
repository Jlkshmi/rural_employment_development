from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from management_app.form import Login_Form, User_Form, Panchayat_Form


# Create your views here.
def intro(request):
    return render(request,'intro.html')

def dash(request):
    return render(request,'dash.html')

def landing_page(request):
    return render(request,'landing_page.html')



def people_reg_page(request):
    form1=Login_Form()
    form2=User_Form()
    if request.method== 'POST':
        form1 =Login_Form(request.POST)
        form2 =User_Form(request.POST)
        if form1.is_valid() and form2.is_valid():
            user=form1.save(commit=False)
            user.is_people = True
            user.save()
            user1= form2.save(commit=False)
            user1.user = user
            user1.save()
            return redirect('login')
    return render(request,'user_reg.html',{'form1':form1,'form2':form2})

def panchayat_reg_page(request):
    form1=Login_Form()
    form2=Panchayat_Form()
    if request.method== 'POST':
        form1=Login_Form(request.POST)
        form2=Panchayat_Form(request.POST)
        if form1.is_valid() and form2.is_valid():
            user= form1.save(commit=False)
            user.is_panchayat = True
            user.save()
            user1= form2.save(commit=False)
            user1.user= user
            user1.save()
            return redirect('login')
    return render(request,'panchayat_reg.html',{'form1':form1,'form2':form2})

def login_view(request):
    if request.method=='POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request,username=username,password=password)
        print(user)

        if user is not None:
            login(request, user)

            if user.is_staff:
                return redirect ('admin_view')
            if user.is_people:
                return redirect('user_profile')
            elif user.is_panchayat:
                return redirect('panchayat_profile')
        else:
            messages.info(request,'Invalid Credentials')
    return render(request,'login_page.html')


def logout_1(request):
    logout(request)
    return redirect('login')