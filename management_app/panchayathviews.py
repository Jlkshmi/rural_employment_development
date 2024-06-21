
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from management_app.form import Panchayat_Form, Job_Form, Work_Form, Payment_Form
from management_app.models import Panchayat, apply_for_job, Job_allotment, work

@login_required(login_url='login')
def panchayath(request):
    return render(request,'panchayath_templates/panchayath.html')
@login_required(login_url='login')
def panchayat_profile(request):
    panchayat= request.user
    data= Panchayat.objects.filter(user=panchayat)
    print(data)
    return render(request,'panchayath_templates/panchayat_profile.html',{'data':data})
@login_required(login_url='login')
def panchayat_update(request,id):
    panchayat = Panchayat.objects.get(id=id)
    form = Panchayat_Form(instance=panchayat)
    if request.method == 'POST':
        form = Panchayat_Form(request.POST, instance=panchayat)
        if form.is_valid():
            form.save()
            return redirect('panchayat_profile')
    return render(request, 'panchayath_templates/panchayat_update.html', {'form': form})
@login_required(login_url='login')
def job_allotment(request):
    job = Job_Form()
    if request.method == 'POST':
        form_1 = Job_Form(request.POST)
        if form_1.is_valid():
            form_1.save()
        return redirect('panchayat_profile')
    return render(request, 'panchayath_templates/job_allotment.html', {'job': job})
@login_required(login_url='login')
def job_allotment_list(request):
    data = Job_allotment.objects.all()
    return render(request,'panchayath_templates/job_allotment_list.html',{'data':data})
@login_required(login_url='login')
def application_accept_view(request):
    status= apply_for_job.objects.filter(status=1)
    return render(request,'panchayath_templates/application_accepted_list.html',{'status':status})
@login_required(login_url='login')
def work_asign(request,id):
    work_1= Work_Form()
    data= apply_for_job.objects.get(id=id)
    asd=data.user
    if request.method=='POST':
        work_2 = Work_Form(request.POST)
        if work_2.is_valid():
            work_3=work_2.save(commit=False)
            work_3.user=asd
            work_3.save()
        return redirect('application_accept_view')
    return render(request,'panchayath_templates/work.html',{'work_1':work_1})
@login_required(login_url='login')
def work_view(request):
    data= work.objects.all()
    return render(request,'panchayath_templates/work_view.html',{'data':data})
@login_required(login_url='login')
def work_update(request,id):
    payment = work.objects.get(id=id)
    form = Work_Form(instance=payment)
    if request.method == 'POST':
        form = Work_Form(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            return redirect('work_view')
    return render(request, 'panchayath_templates/work_update.html', {'form': form})

@login_required(login_url='login')
def payment(request,id):
    payment = Payment_Form()
    # to get that user
    data=work.objects.get(id=id)
    asd=data.user
    if request.method == 'POST':
        form_1 = Payment_Form(request.POST)
        if form_1.is_valid():
            form_2=form_1.save(commit=False)
            form_2.work_id=data
            form_2.user=asd
            form_2.save()
            data.status = 1
            data.save()
        return redirect('work_view')
        messages.info(request, 'Payment Successfully')
    return render(request, 'panchayath_templates/payment_form.html', {'payment': payment})

def work_dlt(request,id):
    data=work.objects.get(id=id)
    data.delete()
    return redirect('work_view')


def status_1(request,id):
    status= work.objects.get(id=id)
    status.status=1
    status.save()
    messages.info(request, 'Payment Successfully')
    return redirect('work_view')
    return render(request,'panchayath_templates/work_view.html')
