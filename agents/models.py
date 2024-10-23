from django.db import models
from django.contrib.auth.models import User , Group


class agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE , primary_key=True)
    agent_name = models.CharField(max_length = 20)
    organisation = models.CharField(max_length = 30 )
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(null=True, max_length=50)

    def __str__(self):
        return f"{self.agent_name}"
    