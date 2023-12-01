# flashcards/models.py
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db import models

class FlashcardSet(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    # Add other fields as needed

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Add any additional fields you need
    # For example:
    birthday = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

class Flashcard(models.Model):
    question = models.TextField()
    answer = models.TextField()
    category = models.CharField(max_length=255)  # You might want to adjust this based on your needs
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='flashcards')  # Add related_name

