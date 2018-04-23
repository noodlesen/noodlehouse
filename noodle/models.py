from django.db import models

# Create your models here.


class Client(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)


class Project(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    asked_amount = models.IntegerField()
    confirmed_amount = models.IntegerField()


class Contract(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)


class Payment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField(default=0)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)


class PortfolioImage(models.Model):
    description = models.CharField(max_length=255)


class PortfolioGallery(models.Model):
    title = models.CharField(max_length=100)



