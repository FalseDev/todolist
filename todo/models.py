import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class todoItem(models.Model):

    class Priority(models.TextChoices):
        LOW = 'LW' , ('Low')
        MEDIUM = 'MD' , ('Medium')
        HIGH = 'HI' , ('High')

    class Colours(models.TextChoices):
        WHITE = 'WHT' , ('White')
        BLACK = 'BLK' , ('Black')
        RED = 'RED' , ('Red')
        GREEN = 'GRN' , ('Green')
        BLUE = 'BLE' , ('Blue')
        YELLOW = 'YLW' , ('Yellow')
        VIOLET = 'VLT' , ('Violet')
        PURPLE = 'PRL' , ('Purple')
        ORANGE = 'ORN' , ('Orange')
        BROWN = 'BRN' , ('Brown')

    owner = models.ForeignKey("todouser" , on_delete=models.CASCADE)
    todo_name = models.CharField(max_length=20 , name='Name')
    todo_text = models.CharField(max_length=400 , name='Text')
    create_date = models.DateTimeField('Date Created')
    todo_priority = models.CharField(
        name = 'Priority' ,
        choices = Priority.choices,
        default = Priority.LOW ,
        max_length = 6
    )

    bg_colour = models.CharField(
        name = 'Colour' ,
        choices = Colours.choices,
        default = Colours.WHITE ,
        max_length = 10
    )

    def __str__(self):
        return self.Name

class todouser(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=78)
#    name = models.CharField(max_length=20)

    def __str__(self):
        return self.username
