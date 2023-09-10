from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    bio = models.TextField(max_length=300, null=True)


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.TextField(max_length=50)


class Listing(models.Model):
    id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=200, null=False)
    starting_price = models.IntegerField()
    listed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    image = models.TextField(null=True, blank=True, default=None)
    description = models.TextField(max_length=400, null=True, blank=True, default=None)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Bid(models.Model):
    id = models.AutoField(primary_key=True)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    bid = models.IntegerField(null = False)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    comment = models.TextField(max_length=500)
