from django.db import models

# Create your models here.
class login(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    type = models.CharField(max_length=10)

#
# class register(models.Model):
#     name = models.CharField(max_length=30)
#     password = models.CharField(max_length=30)
#     type = models.CharField(max_length=10)
    # shopname = models.CharField(max_length=10)
    # email = models.CharField(max_length=10)
    # Category = models.CharField(max_length=10)
    # FLOOR = models.CharField(max_length=10)


class floor(models.Model):
    floorno= models.CharField(max_length=10)

class category(models.Model):
    Category=models.CharField(max_length=30,default="none")

class shop(models.Model):
    shopname = models.CharField(max_length=30)
    shopnumber = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    Category = models.CharField(max_length=30,default="none")
    logo = models.CharField(max_length=300)
    phonenumber = models.CharField(max_length=30)
    FLOOR = models.ForeignKey(floor,on_delete=models.CASCADE)
    LOGIN = models.ForeignKey(login,on_delete=models.CASCADE,default=1)
    x_axis=models.IntegerField(max_length=30,default="none")
    y_axis=models.IntegerField(max_length=30,default="none")


    type = models.CharField(max_length=30, default="none")


class direction(models.Model):
    # id = models.CharField(max_length=30)
    shopida=  models.ForeignKey(shop,on_delete=models.CASCADE,related_name="shopida")
    shopidb =  models.ForeignKey(shop,on_delete=models.CASCADE,related_name="shopidb")
    direction = models.CharField(max_length=30)




class hotspot(models.Model):
    SHOP = models.ForeignKey(shop,on_delete=models.CASCADE)
    hotspotaddress= models.CharField(max_length=30)



class product(models.Model):
    SHOP = models.ForeignKey(shop,on_delete=models.CASCADE)
    productname = models.CharField(max_length=30)
    stock = models.CharField(max_length=30)
    price = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    photo = models.CharField(max_length=30)



class offers(models.Model):
    PRODUCT = models.ForeignKey(product,on_delete=models.CASCADE)
    offer = models.CharField(max_length=30)
    date = models.CharField(max_length=30)
    validtill = models.CharField(max_length=30)
    description = models.CharField(max_length=30)


class notification(models.Model):
    notification = models.CharField(max_length=30)
    shop_id= models.ForeignKey(shop, on_delete=models.CASCADE,default=35)

    # time = models.CharField(max_length=30)
    # date = models.DateField(max_length=10)
    # status = models.CharField(max_length=10)


class user(models.Model):
    firstname = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phonenumber = models.CharField(max_length=30)
    LOGIN =  models.ForeignKey(login,on_delete=models.CASCADE)


class feedback(models.Model):
    USER = models.ForeignKey(user,on_delete=models.CASCADE)
    feedback = models.CharField(max_length=30)
    date=models.DateField()


class complaint(models.Model):
    USER = models.ForeignKey(user, on_delete=models.CASCADE)
    complaint = models.CharField(max_length=100)
    reply = models.CharField(max_length=100)
    date = models.CharField(max_length=10)
    status = models.CharField(max_length=10)


class emergencymessage(models.Model):
    USER = models.ForeignKey(user, on_delete=models.CASCADE)
    emergencymessage = models.CharField(max_length=30)
    reply = models.CharField(max_length=30)
    time = models.CharField(max_length=30)
    date = models.CharField(max_length=100)
    status = models.CharField(max_length=10)


