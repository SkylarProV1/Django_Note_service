# Register your models here.
from django.contrib import admin
from .models import Note

#admin.site.register(Note)


class NoteAdmin(admin.ModelAdmin):
    list_display = ('title','owner','pub_date', 'was_published_recently')
    list_filter = ['pub_date']

# Replace your other register call with this line:
admin.site.register(Note, NoteAdmin)