from django.db import models

# Create your models here.


class Client(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)


class Project(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    client = models.ForeignKey(Client)
    asked_amount = models.IntegerField()
    confirmed_amount = models.IntegerField()


class Contract(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Client)


class Payment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField(default=0)
    #project = models.ForeignKey(Project, null=True)
    #client = models.ForeignKey(Client)
    contract = models.ForeignKey(Contract)

