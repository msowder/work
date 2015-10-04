# import datetime

# from django.db import models
# from django.utils import timezone


# class Tasks(models.Model):
#     name = models.CharField(max_length=200)
#     category = models.CharField(max_length=200)
#     points = models.IntegerField(default=0)
#     due_date = models.DateTimeField()
#     difficulty = models.CharField(max_length=200)


# class Rewards(models.Model):
#     name = models.CharField(max_length=200)
#     category = models.CharField(max_length=200)
#     points = models.IntegerField(default=0)
#     priority = models.CharField(max_length=200)
#     difficulty = models.CharField(max_length=200)
#     start_time = models.DateTimeField()
#     end_time = models.DateTimeField()


# class Account(models.Model):
#     # get this info from login/assicaiate and take from google
#     # can we store the bedtime/hours of sleep?
#     # can this be saved for next time the person logs in?
#     # should tasks also be added to this?
#     name = models.CharField(max_length=200)
#     photo = models.FilePathField(path=None, match=None, recursive=False) #idk if this is how this is done
#     points = models.IntegerField(default=0)

import django
import datetime
import cgi

from django.db import models
from django.utils import timezone


#write algorithm depending on difficulty (and what points are added)
#populate data table
#for loop that puts info on website (help me)
#form w/ name, drop down with category + difficulty

class Tasks(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    points = models.IntegerField(default=0)
    due_date = models.DateTimeField()
    difficulty = models.CharField(max_length=200)

    # formData = cgi.FieldStorage()
    # nameInput = formData.getValue('shipping[first-name]') #might need to change
    # name = name + nameInput

class Rewards(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    points = models.IntegerField(default=0)
    #priority = models.CharField(max_length=200)
    priority = models.CharField(max_length=200)


    #maybe not need!
    #start_time = models.DateTimeField()
    #end_time = models.DateTimeField()

    # May need later
    #  def __str__(self):
    #     return self.choice_text


class Calendar(models.Model):
    # somehow need to get this data from the data table and the tasks table--
    # tasks table probs need to have all this data
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


class Account(models.Model):
    # get this info from login/assicaiate and take from google
    # can we store the bedtime/hours of sleep?
    # can this be saved for next time the person logs in?
    # should tasks also be added to this?
    name = models.CharField(max_length=200)
    photo = models.FilePathField(path=None, match=None, recursive=False) #idk if this is how this is done
    points = models.IntegerField(default=0)