from django.db import models
class Contact(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class PhoneNumber(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    phone = models.IntegerField()

    def __str__(self):
        return str(self.phone)



