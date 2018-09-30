from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Team(models.Model):
    team_name = models.CharField(max_length=250)
    team_project = models.CharField(max_length=250)
    bio = models.TextField(max_length=1000)
    vote_count = models.PositiveIntegerField(default=0)
    is_voted = models.BooleanField(default=False)

    def __str__(self):
        return self.team_name

    def get_absolute_url(self):
        return reverse('dashapp:team_details', kwargs={'pk':self.pk})

class Members(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    fName = models.CharField(max_length=50)
    lName = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('dashapp:team_details', kwargs={'pk':self.pk})

class MalePresenter(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    fName = models.CharField(max_length=50)
    lName = models.CharField(max_length=50)
    vote_count = models.PositiveIntegerField(default=0)
    is_voted = models.BooleanField(default=False)

    def __str__(self):
        return self.fName+' '+self.lName
    
    def get_absolute_url(self):
        return reverse('dashapp:female_presenters')
    
class FemalePresenter(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    fName = models.CharField(max_length=50)
    lName = models.CharField(max_length=50)
    vote_count = models.PositiveIntegerField(default=0)
    is_voted = models.BooleanField(default=False)

    def __str__(self):
        return self.fName+' '+self.lName
    
    def get_absolute_url(self):
        return reverse('dashapp:female_presenters')
    
