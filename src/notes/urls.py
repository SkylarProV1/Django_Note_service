from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from .views import (NoteList, NoteDetail,NoteCreate,
NoteUpdate,NoteDelete,TagView,SearchView,SharingNote,SharingTag,SharingSearch)

app_name = 'notes'

urlpatterns = [
	path('', NoteList.as_view(), name='index'),
    path('<int:pk>/', NoteDetail.as_view(), name='detail'),
    path('new/', NoteCreate.as_view(), name='create'),
    path('<int:pk>/edit/', NoteUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', NoteDelete.as_view(), name='delete'),
    path('tag/<slug>', TagView.as_view(), name='tagged'),
    path('search/', SearchView.as_view(), name='searched'),
    path('public/', SharingNote.as_view(),name='shared'),
    path('public/tag/<slug>', SharingTag.as_view(),name='sharedtag'),
    path('public/search/', SharingSearch.as_view(),name='sharedsearch')
] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)