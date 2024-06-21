from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from management_app.form import Schemes_Form, Noti_Form
from management_app.models import Panchayat, People, Schemes, Feedback, apply_for_job, Notification

@login_required(login_url='login')
def admin(request):
    return render(request,'admin_templates/admin.html')
@login_required(login_url='login')
def user_view(request):
    data= People.objects.all()
    return render(request,'admin_templates/user_list_view.html',{'data':data})
@login_required(login_url='login')
def panchayat_view(request):
    data1 = Panchayat.objects.all()
    return render(request,'admin_templates/panchayat_list_view.html',{'data1':data1})
@login_required(login_url='login')
def scheme_view(request):
    scheme= Schemes.objects.all()
    return render(request,'admin_templates/schemes_list.html',{'scheme':scheme})
@login_required(login_url='login')
def add_schemes(request):
    form= Schemes_Form()
    if request.method == 'POST':
        form_1=Schemes_Form(request.POST)
        if form_1.is_valid():
            form_1.save()
        return redirect('scheme_list_view')
    return render(request,'admin_templates/add_schemes.html',{'form':form})
@login_required(login_url='login')
def scheme_dlt(request,id):
    data= Schemes.objects.get(id=id)
    data.delete()
    return redirect('scheme_list_view')

@login_required(login_url='login')
def feedback_view(request):
    data= Feedback.objects.all()
    return render(request,'admin_templates/feedback_view.html',{'data':data})
@login_required(login_url='login')
def feedback_reply(request,id):
    feedback_reply=Feedback.objects.get(id=id)
    if request.method=='POST':
        reply_1=request.POST.get('reply')
        feedback_reply.reply=reply_1
        feedback_reply.save()
        return redirect('feedback_view')
    return render(request,'admin_templates/feedback_reply.html',{'feedback_reply':feedback_reply})

@login_required(login_url='login')
def application_view(request):
    data= apply_for_job.objects.all()
    return render(request,'admin_templates/job_applications.html',{'data':data})
@login_required(login_url='login')
def status_change_1(request,id):
    status = apply_for_job.objects.get(id=id)
    status.status = 1
    status.save()
    return redirect('job_application')
    return render(request,'admin_templates/job_applications.html')
@login_required(login_url='login')
def status_change_2(request,id):
    status = apply_for_job.objects.get(id=id)
    status.status = 2
    status.save()
    return redirect('job_application')
    return render(request,'admin_templates/job_applications.html')

@login_required(login_url='login')
def notification(request):
    form= Noti_Form()
    if request.method == 'POST':
        form_1=Noti_Form(request.POST)
        if form_1.is_valid():
            form_1.save()
        return redirect('admin_view')
    return render(request,'admin_templates/notification.html',{'form':form})
@login_required(login_url='login')
def notification_view(request):
    data = Notification.objects.all()
    return render(request,'admin_templates/notification_view.html',{'data':data})

@login_required(login_url='login')
def noti_dlt(request,id):
    data= Notification.objects.get(id=id)
    data.delete()
    return redirect('notification_view')

def noti_update(request,id):
    noti = Notification.objects.get(id=id)
    form = Noti_Form(instance=noti)
    if request.method == 'POST':
        form = Noti_Form(request.POST, instance=noti)
        if form.is_valid():
            form.save()
            return redirect('notification_view')
    return render(request, 'admin_templates/notification_update.html', {'form': form})

