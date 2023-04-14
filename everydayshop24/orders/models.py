from django.db import models


class Customer(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=200)

    def __str__(self):
        return "%s %s" % (self.name, self.email)
