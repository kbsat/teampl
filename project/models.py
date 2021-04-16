from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    cid = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=60, null=True)

    def __str__(self):
        return str(self.category_name)


class Project(models.Model):
    pid = models.AutoField(primary_key=True)
    userid = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=60)
    sub_title = models.TextField(max_length=100, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    pub_date = models.DateTimeField(default=timezone.now)
    hit = models.PositiveIntegerField(default=0, null=True, blank=True)
    done = models.BooleanField(default=False)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.pid)


class Comment(models.Model):
    pid = models.ForeignKey(Project, on_delete=models.CASCADE)
    userid = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    pub_date = models.DateTimeField(default=timezone.now)
    comment = models.CharField(max_length=300)

    def __str__(self):
        return str(self.comment)


class Role(models.Model):
    role_name = models.CharField(max_length=60, null=True)

    def __str__(self):
        return str(self.role_name)


class Apply(models.Model):
    userid = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pid = models.ForeignKey(Project, on_delete=models.CASCADE)
    role = models.ForeignKey(
        Role, on_delete=models.CASCADE, null=True)
    body = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return str(self.userid)+" apply project"+str(self.pid)


class Assign(models.Model):
    userid = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pid = models.ForeignKey(Project, on_delete=models.CASCADE)
    role = models.ForeignKey(
        Role, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.userid)+"-"+str(self.pid)
