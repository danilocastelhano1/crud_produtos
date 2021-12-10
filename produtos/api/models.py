from django.db import models
from django.contrib.auth.models import User


class Produto(models.Model):
    id = models.AutoField(primary_key=True, max_length=10)
    owner = models.ForeignKey(User, null=False, on_delete=models.CASCADE, related_name='user_owner', verbose_name="User")
    created_datetime = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=60, null=False, verbose_name="Title")
    content = models.CharField(max_length=200, null=False, verbose_name="Content")
    price = models.FloatField(null=False, verbose_name="Price")
