from .models import Note

from taggit.models import Tag

class NoteMixin(object):
	
	def get_context_data(self, **kwargs):
		context = super(NoteMixin, self).get_context_data(**kwargs)

		context.update({
			'notes': Note.objects.filter(owner=self.request.user).order_by('-pub_date'),
			})
		return context

class TagMixin(object):

	def get_context_data(self, **kwargs):
		context = super(TagMixin, self).get_context_data(**kwargs)
		context['tags']=Tag.objects.all()
		return context