from django.shortcuts import render

from rest_framework.renderers import JSONRenderer

from rest_framework import generics

from rest_framework import viewsets
from rest_framework import permissions
from notes.models import Note
from .serializers import NoteSerializer
# Create your views here.

class NoteViewSet(viewsets.ModelViewSet):

	serializer_class = NoteSerializer 
	queryset = Note.objects.all()

	def filter_queryset(self, queryset):
		queryset = Note.objects.filter(owner=self.request.user)
		tag = self.request.query_params.get('tags', None)
		if tag is not None:
			queryset = queryset.filter(tags=tag)
		return queryset




	"""
class NoteViewSet(generics.ListAPIView):

	serializer_class = NoteSerializer 
	queryset = Note.objects.all()
	permission_classes = [permissions.IsAuthenticated]
	renderer_classes = [JSONRenderer]

	def filter_queryset(self, queryset):
		queryset = Note.objects.filter(owner=self.request.user)
		return queryset

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

	"""
