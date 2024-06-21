from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from management_app.form import User_Form, Feedback_Form
from management_app.models import People, Job_allotment, apply_for_job, Feedback, Notification, Payment


@login_required(login_url='login')
def people(request):
    return render(request,'people_templates/people.html')

@login_required(login_url='login')
def user_profile(request):
    user_1 = request.user
    data = People.objects.filter(user=user_1)
    return render(request,'people_templates/user_profile.html',{'data':data})

@login_required(login_url='login')
def user_delete(request,id):
    data= People.objects.get(id=id)
    data.delete()
    return redirect('user_list_view')

@login_required(login_url='login')
def user_update(request,id):
    user=People.objects.get(id=id)
    form = User_Form(instance=user)
    if request.method=='POST':
        form=User_Form(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    return render(request,'people_templates/user_update.html',{'form':form})

@login_required(login_url='login')
def job_list_view(request):
    data = Job_allotment.objects.all()
    return render(request,'people_templates/Job_allotment_lists.html',{'data':data})

@login_required(login_url='login')
def job_apply(request,id):
    slot= Job_allotment.objects.get(id=id)
    u = People.objects.get(user=request.user)
    apply = apply_for_job.objects.filter(user=u,job=slot)
    if apply.exists():
        messages.info(request,'You have already applied for this job')
        return redirect('job_list_view')
    else:
        if request.method == 'POST':
            obj = apply_for_job()
            obj.user = u
            obj.job = slot
            obj.save()
            messages.info(request,'Applied Successfully')
            return redirect('user_profile')
        return render(request,'people_templates/apply_for_job.html',{'slot':slot})

@login_required(login_url='login')
def add_feedback(request):
    # to save the user
    form=Feedback_Form()
    user=request.user
    if request.method == 'POST':
        data = Feedback_Form(request.POST)
        if data.is_valid():
            feedback=data.save(commit=False)
            feedback.user=user
            feedback.save()
            return redirect('user_profile')
    return render(request,'people_templates/add_feedback.html',{'form_1':form})

@login_required(login_url='login')
def reply_view(request):
    data=Feedback.objects.all()
    return render(request,'people_templates/reply_view.html',{'data':data})

@login_required(login_url='login')
def application_reply(request):
    user_1=request.user
    people= People.objects.get(user=user_1)
    print(people)
    data= apply_for_job.objects.filter(user=people)
    return render(request,'people_templates/application_reply.html',{'data':data})

@login_required(login_url='login')
def noti_view(request):
    data=Notification.objects.all()
    return render(request,'people_templates/notification_view.html',{'data':data})

@login_required(login_url='login')
def receive_payment(request):
    user_1=request.user
    people= People.objects.get(user=user_1)
    data= Payment.objects.filter(user=people)
    return render(request,'people_templates/user_payment.html',{'data':data})

