from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    cat = models.CharField(max_length=255)
    price = models.IntegerField()
    quant = models.IntegerField()
    image_url = models.CharField(max_length=2083)

    def __str__(self):
        return self.title



class Fibuy(models.Model):
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.IntegerField()
    prod_id=models.CharField(null=True ,max_length=255)

    def __str__(self):
        return self.email


class Sell(models.Model):
    prod_id = models.CharField(max_length=255)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    money = models.IntegerField()
    address = models.CharField(max_length=255)
    cate = models.CharField(max_length=255)
    phone = models.IntegerField()
    year = models.IntegerField()

    def __str__(self):
        return self.phone