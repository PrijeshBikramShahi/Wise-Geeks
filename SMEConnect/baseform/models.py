from django.db import models
from users.models import User
from django.utils import timezone

class investor(models.Model):
    investor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="investor")
    inverstorname = models.CharField(max_length=200, blank=True, null= True)
    email = models.EmailField()
    linkedin = models.URLField()
    firmName = models.CharField(max_length=200)
    bio = models.TextField()
    reg_Date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.inverstorname

class startup(models.Model):
    startup = models.ForeignKey(User, on_delete=models.CASCADE, related_name="startup")
    startup_name = models.CharField(max_length=200)
    email = models.EmailField()
    weburl = models.URLField()
    des = models.TextField()
    linkedin = models.URLField()
    reg_no = models.IntegerField()
    reg_certificate = models.FileField(upload_to='media/certificates')
    year_founded = models.IntegerField()
    teamSize = models.IntegerField()
    businessPlan = models.FileField(upload_to='media/businessplan')
    pitchVideos = models.FileField(upload_to='media/pitchvideos', blank=True, null=True)
    reg_Date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username