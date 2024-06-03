from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_people=models.BooleanField(default=False)
    is_panchayat=models.BooleanField(default=False)




class People(models.Model):
    user=models.ForeignKey(Login,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    contact_no=models.IntegerField()
    email=models.EmailField()
    address=models.TextField()
    qualification=models.TextField()
    age=models.IntegerField()
    experience=models.TextField()



    def __str__(self):
        return self.name

class Panchayat(models.Model):
    user=models.ForeignKey(Login,on_delete=models.CASCADE)
    panchayath_name=models.CharField(max_length=100)
    location=models.TextField()
    district=models.TextField()

class Schemes(models.Model):
    name=models.CharField(max_length=100)
    ministry=models.TextField()
    remarks=models.TextField()
    distribution=models.IntegerField()

    def __str__(self):
        return self.name

class Job_allotment(models.Model):
    scheme=models.ForeignKey(Schemes,on_delete=models.CASCADE)
    job_title=models.CharField(max_length=100)
    requirements=models.TextField()
    experience=models.TextField()

class apply_for_job(models.Model):
    user = models.ForeignKey(People,on_delete=models.CASCADE)
    job = models.ForeignKey(Job_allotment,on_delete=models.CASCADE)
    status = models.IntegerField(default=0)



class Feedback(models.Model):
    user= models.ForeignKey(Login,on_delete=models.CASCADE)
    date=models.DateField(auto_now=True)
    feedback=models.TextField()
    reply=models.TextField(null=True,blank=True)


class Report(models.Model):
    scheme = models.ForeignKey(Schemes, on_delete=models.CASCADE)
    report= models.TextField()


class Notification(models.Model):
    notification= models.TextField()

class work(models.Model):
    user=models.ForeignKey(People,on_delete=models.CASCADE,null=True,blank=True)
    scheme=models.ForeignKey(Schemes, on_delete=models.CASCADE)
    work_title=models.CharField(max_length=100)
    start_date=models.DateField()
    end_date=models.DateField()
    cat=(('work started','work started'),('10% finished','10% finished'),('30% finished','30% finished'),('50% finished','50% finished'),('75% finished','75% finished'),('100% finished','100% finished'))
    complete=models.CharField(max_length=50,choices=cat)
    status=models.IntegerField(default=0)


    def __str__(self):
        return self.user.name




class Payment(models.Model):
    work_id=models.ForeignKey(work,on_delete=models.CASCADE,null=True,blank=True)
    user=models.ForeignKey(People,on_delete=models.CASCADE)
    account_number=models.IntegerField()
    IFSC_code=models.CharField()
    amount=models.IntegerField()

