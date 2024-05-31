from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import DateInput

from management_app.models import Login, Panchayat, People, Schemes, Job_allotment, Feedback, Report, Notification, \
    work, Payment


class DateInput(forms.DateInput):
    input_type = 'date'
class Login_Form(UserCreationForm):
    class Meta:
        model=Login
        fields=('username','password1','password2')

class User_Form(forms.ModelForm):
    class Meta:
        model=People
        fields=('name','contact_no','email','address','qualification','age','experience')

class Panchayat_Form(forms.ModelForm):
    class Meta:
        model=Panchayat
        fields=('panchayath_name','location','district')

class Schemes_Form(forms.ModelForm):
    class Meta:
        model=Schemes
        fields=('name','ministry','remarks','distribution')

class Job_Form(forms.ModelForm):
    class Meta:
        model=Job_allotment
        fields=('scheme','job_title','requirements','experience')

class Feedback_Form(forms.ModelForm):
    class Meta:
        model=Feedback
        fields=('feedback',)

class Report_Form(forms.ModelForm):
    class Meta:
        model=Report
        fields=('scheme','report')

class Noti_Form(forms.ModelForm):
    class Meta:
        model=Notification
        fields=('notification',)

class Work_Form(forms.ModelForm):
    start_date = forms.DateField(widget=DateInput, )
    end_date = forms.DateField(widget=DateInput, )
    class Meta:
        model= work
        fields=('scheme','work_title','start_date','end_date','complete')

class Payment_Form(forms.ModelForm):
    class Meta:
        model= Payment
        fields=('account_number','IFSC_code','amount')