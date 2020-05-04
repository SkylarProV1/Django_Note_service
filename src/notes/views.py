from django.utils.decorators import method_decorator
from django.urls import reverse
from django.contrib.auth.decorators import login_required 

from django.views.generic import (ListView, DetailView,
	CreateView,UpdateView,DeleteView)

from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.urls import reverse_lazy

from .forms import NoteForm
from .models import Note
from .mixins import NoteMixin,TagMixin

from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import slugify

from taggit.models import Tag
# Create your views here


class NoteList(LoginRequiredMixin,TagMixin,ListView):
	paginate_by = 5
	template_name = 'notes/index.html'
	context_object_name = 'latest_note_list'

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(NoteList, self).dispatch(*args, **kwargs)

	def get_queryset(self):
		return Note.objects.filter(owner=self.request.user).order_by('-pub_date')


class NoteDetail(LoginRequiredMixin,DetailView):
	model = Note
	template_name = 'notes/detail.html'
	context_object_name = 'note'

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(NoteDetail, self).dispatch(*args, **kwargs)

	def get_queryset(self):
		return Note.objects.filter(owner=self.request.user)


class NoteCreate(LoginRequiredMixin,NoteMixin, CreateView):
	form_class = NoteForm
	template_name = 'notes/form.html'
	success_url = reverse_lazy('notes:index')


	def form_valid(self, form):
		form.instance.owner = self.request.user
		form.instance.pub_date = timezone.now()
		return super(NoteCreate, self).form_valid(form)


class NoteUpdate(LoginRequiredMixin,NoteMixin, UpdateView):
	model = Note
	form_class = NoteForm
	template_name = 'notes/form.html'

	def get_queryset(self):
		return Note.objects.filter(owner=self.request.user)

	def get_success_url(self):
		return reverse('notes:update', kwargs={
			'pk': self.object.pk
			})

class NoteDelete(LoginRequiredMixin, DeleteView):
	model = Note
	success_url = reverse_lazy('notes:create')

	def get_queryset(self):
		return Note.objects.filter(owner=self.request.user)


class TagView(LoginRequiredMixin,TagMixin,ListView):
	template_name='notes/index.html'
	model = Note
	paginate_by = 5
	context_object_name = 'latest_note_list'
	

	def get_queryset(self):
		resp=Note.objects.filter(owner=self.request.user)
		return resp.filter(tags__slug=self.kwargs.get('slug'))


class SearchView(LoginRequiredMixin,TagMixin,ListView):
	template_name='notes/index.html'
	model = Note
	paginate_by = 5
	context_object_name = 'latest_note_list'


	def get_queryset(self):
		resp=Note.objects.filter(owner=self.request.user)
		query = self.request.GET.get('q')
		return resp.filter(title__icontains=query)


class SharingNote(LoginRequiredMixin,TagMixin,ListView):
	template_name='notes/public.html'
	model = Note
	paginate_by = 5
	context_object_name = 'latest_note_list'

	def get_queryset(self):
		return Note.objects.filter(public__icontains=True)


class SharingTag(LoginRequiredMixin,TagMixin,ListView):
	template_name='notes/public.html'
	model = Note
	context_object_name = 'latest_note_list'

	def get_queryset(self):
		resp=Note.objects.filter(public__icontains=True)
		return resp.filter(tags__slug=self.kwargs.get('slug'))


class SharingSearch(LoginRequiredMixin,TagMixin,ListView):
	template_name='notes/public.html'
	model = Note
	context_object_name = 'latest_note_list'

	def get_queryset(self):
		resp=Note.objects.filter(public__icontains=True)
		query = self.request.GET.get('q')
		return resp.filter(title__icontains=query)






