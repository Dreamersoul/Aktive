from django.db import models
from django.contrib.auth.models import User
from geoposition.fields import GeopositionField


class Profile(models.Model):
    profile_user = models.OneToOneField(User, related_name='profile_user')
    phoneNumber = models.CharField(max_length=30, null=True, blank=True)
    badges = models.ManyToManyField('Badge', null=True, blank=True)
    interests = models.ManyToManyField('Category', related_name='interests', null=True, blank=True)
    picture = models.ImageField(upload_to="users", null=True, blank=True)

    def __unicode__(self):
        return self.profile_user.username


class Agent(models.Model):
    profile = models.OneToOneField(User, related_name='profile')
    phoneNumber = models.CharField(max_length=30)
    website = models.CharField(max_length=200)

    def __unicode__(self):
        return self.profile.username


class Activity(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    location = GeopositionField(null=True)
    userCount = models.IntegerField(default=0)
    startDate = models.DateTimeField(null=True, blank=True)
    endDate = models.DateTimeField(null=True, blank=True)
    price = models.FloatField(null=True)
    isActivity = models.BooleanField()
    agent = models.ForeignKey('Agent')
    users = models.ManyToManyField('Profile', blank=True)
    category = models.ForeignKey('Category')
    image = models.ImageField(upload_to='activity')

    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    badge = models.OneToOneField('Badge', null=True, blank=True)

    def __unicode__(self):
        return self.name


class Badge(models.Model):
    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to="Badges", blank=True)

    def __unicode__(self):
        return self.name