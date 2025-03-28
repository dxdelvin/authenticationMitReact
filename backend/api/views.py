from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import NoteSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny  
from .models import Note

class NoteListCreate(generics.CreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]  
    
    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)

    def perform_create(self, serializer):
        user = self.request.user
        if serializer.is_valid():
            serializer.save(author=user)
        else:
            print(serializer.errors)
            
class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]  
    
    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
    
                
# Create your views here.
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]