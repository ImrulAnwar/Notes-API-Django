from django.urls import path
from .views import NoteView, NoteDetailView

urlpatterns = [
    path('notes/', NoteView.as_view(), name='all_notes'),
    path('notes/<int:note_id>/', NoteDetailView.as_view(), name='get_note'),
]