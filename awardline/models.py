from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from tinymce.models import HTMLField
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.conf import settings
from django.db.models import Avg, Max, Min
import numpy as np



def post_save_user_model(sender,instance,created,*args,**kwargs):
    if created:
        try:
            Profile.objects.create(user = instance)
        except:
            pass
post_save.connect(post_save_user_model,sender=settings.AUTH_USER_MODEL)

class Profile(models.Model):
    profile_image = models.ImageField(blank=True,upload_to='profiles/')
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')


    def save_profile(self):
        self.save()


    @classmethod
    def get_by_id(cls, id):
        profile = Profile.objects.get(user = id)
        return profile

    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user = id).first()
        return profile

    def get_absolute_url(self):
        return reverse('user_profile')

  
    def __str__(self):
        return self.user

class Project(models.Model):
   """
   This is the class we will use to create images
   """
   image_url = models.ImageField(upload_to = "images/")
   title = models.CharField(max_length = 30)
   description = HTMLField()
   poster = models.ForeignKey(User,related_name='images')
   date = models.DateTimeField(auto_now_add = True,null = True)
   url = models.URLField(max_length = 100)

   def average_design(self):
        design_ratings = list(map(lambda x: x.design_rating, self.reviews.all()))
        return np.mean(design_ratings)

   def average_usability(self):
        usability_ratings = list(map(lambda x: x.usability_rating, self.reviews.all()))
        return np.mean(usability_ratings)

   def average_content(self):
        content_ratings = list(map(lambda x: x.content_rating, self.reviews.all()))
        return np.mean(content_ratings)

   @classmethod
   def search_project(cls,name):
        project = Project.objects.filter(title__icontains = name)
        return project


   def save_project(self):
       """
       This is the function that we will use to save the instance of this class
       """
       self.save()

   def delete_project(self):
       """
       This is the function that we will use to delete the instance of this class
       """
       self.delete()

   def __str__(self):
       return self.title



class Comments(models.Model):
    text = models.CharField(max_length = 100, blank = True)
    project = models.ForeignKey(Project, related_name = "comments")
    author = models.ForeignKey(User, related_name = "author")
    created_date = models.DateTimeField(auto_now_add = True,null = True)


    def save_comment(self):
       """
       This is the function that we will use to save the instance of this class
       """
       self.save()

    def delete_comment(self):
        Comments.objects.get(id = self.id).delete()

    @classmethod
    def get_comments_by_projects(cls, id):
        comments = Comments.objects.filter(project__pk = id)
        return comments

    def __str__(self):
        return self.text

class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),

    )
    project = models.ForeignKey(Project, null=True, blank=True, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='reviews')
    comment = models.TextField()
    design_rating = models.IntegerField(choices=RATING_CHOICES, default=0)
    usability_rating = models.IntegerField(choices=RATING_CHOICES, default=0)
    content_rating = models.IntegerField(choices=RATING_CHOICES, default=0)
    created_date = models.DateTimeField(auto_now_add = True,null = True)

    def save_review(self):
        self.save()

    def delete_comment(self):
        Review.objects.get(id = self.id).delete()

    @classmethod
    def get_comment(cls, id):
        comments = Review.objects.filter(project__pk =id)
        return comments

    def delete_review(self):
        self.delete()

    def __str__(self):
        return self.comment
