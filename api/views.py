from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Note
from .serializers import NoteSerializer

class NoteView(APIView):
    def get(self, request):
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many = True)
        return Response(serializer.data)
    
class NoteDetailView(APIView):
    def get(self, request, note_id):
        note = Note.objects.get(id = note_id)
        serializer = NoteSerializer(note)
        return Response(serializer.data)