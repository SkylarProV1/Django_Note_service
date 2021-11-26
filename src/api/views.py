from django.shortcuts import render

from rest_framework.response import Response

from rest_framework.renderers import JSONRenderer

from rest_framework import generics,status

from rest_framework.decorators import action

from rest_framework import viewsets
from rest_framework import permissions
from notes.models import Note
from accounts.models import User
from .serializers import NoteSerializer,PublicSerializer,RegisterSerializer

from rest_framework.decorators import api_view
# Create your views here.

from django.http import HttpResponse
#from snippets.serializers import SnippetSerializer

from accounts.forms import UserCreationForm
from django.shortcuts import render, redirect

from django.contrib.auth import get_user_model


class NoteViewSet(viewsets.ModelViewSet):

	serializer_class = NoteSerializer
	queryset = Note.objects.all()
	permission_classes = [permissions.IsAuthenticated]
	renderer_classes = [JSONRenderer]

	def filter_queryset(self, queryset):
		queryset = Note.objects.filter(owner=self.request.user)
		return queryset

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

	def perform_destroy(self, instance):
		instance.delete()

	def perform_update(self, serializer):
		serializer.save()


class TageViewSet(viewsets.ModelViewSet):
	serializer_class = NoteSerializer 
	queryset = Note.objects.all()
	permission_classes = [permissions.IsAuthenticated]
	renderer_classes = [JSONRenderer]

	def filter_queryset(self, queryset):
		queryset = Note.objects.filter(owner=self.request.user)
		return queryset.filter(tags__slug=self.kwargs.get('slug'))

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)



class SearchNotesSet(viewsets.ModelViewSet):
	serializer_class = NoteSerializer 
	queryset = Note.objects.all()
	permission_classes = [permissions.IsAuthenticated]
	renderer_classes = [JSONRenderer]

	def filter_queryset(self, queryset):

		queryset=Note.objects.filter(owner=self.request.user)
		query = self.request.GET.get('q')
		return queryset.filter(title__icontains=query)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

class SearchPublicNoteSet(viewsets.ModelViewSet):
	serializer_class = NoteSerializer 
	queryset = Note.objects.all()
	permission_classes = [permissions.IsAuthenticated]
	renderer_classes = [JSONRenderer]

	def filter_queryset(self, queryset):
		queryset=Note.objects.filter(public__icontains=True)
		query = self.request.GET.get('q')
		return queryset.filter(title__icontains=query)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

class SherachPublicTag(viewsets.ModelViewSet):
	serializer_class = NoteSerializer 
	queryset = Note.objects.all()
	permission_classes = [permissions.IsAuthenticated]
	renderer_classes = [JSONRenderer]

	def filter_queryset(self, queryset):
		queryset = Note.objects.filter(public__icontains=True)
		return queryset.filter(tags__slug=self.kwargs.get('slug'))

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

class Public(viewsets.ModelViewSet):
	serializer_class = NoteSerializer 
	queryset = Note.objects.all()
	permission_classes = [permissions.IsAuthenticated]
	renderer_classes = [JSONRenderer]

	def filter_queryset(self, queryset):
		return Note.objects.filter(public__icontains=True)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)


class Register(viewsets.ModelViewSet):

	model = get_user_model()
	serializer_class = RegisterSerializer
	permission_classes = [permissions.AllowAny]

	def perform_create(self,serializer):
		serializer.save()
