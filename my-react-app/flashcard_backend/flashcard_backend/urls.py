# flashcard_backend/urls.py
from django.http import HttpResponse
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('flashcards.urls')),
    path('', lambda request: HttpResponse("Welcome to the Flashcard Backend!"), name='home'),
]

