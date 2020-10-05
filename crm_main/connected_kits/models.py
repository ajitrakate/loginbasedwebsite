from django.db import models
from django.contrib.auth.models import User

homeautomation = User.objects.get(pk=1)
# Create your models here.
class Kit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    manufacturer_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)

    def __str__(self):
        return  "{} {}".format(self.user, self.user_name)

class Button(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    kit = models.ForeignKey(Kit, on_delete=models.CASCADE)
    pin_no = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=20)

    def __str__(self):
        return "{} {} ".format(self.user, self.kit)


