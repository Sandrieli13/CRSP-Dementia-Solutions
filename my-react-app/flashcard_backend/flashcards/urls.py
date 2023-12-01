# flashcards/urls.py
from django.urls import path
from .views import FlashcardListCreateView, LoginAPIView, FlashcardSetListCreateView

urlpatterns = [
    path('api/flashcard-sets/', FlashcardSetListCreateView.as_view(), name='flashcard-set-list-create'),
    path('flashcards/', FlashcardListCreateView.as_view(), name='flashcard-list-create'),
    path('api/login/', LoginAPIView.as_view(), name='api-login'),
]
