from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter

from . import views

from .views import NoteViewSet,TageViewSet, SearchNotesSet, SearchPublicNoteSet,SherachPublicTag,Public,Update,Register

app_name = 'api'

router = DefaultRouter(trailing_slash=False)



router.register(r'notes', NoteViewSet)
router.register(r'register',Register,base_name='User')

urlpatterns = [
	path('jwt-auth/', obtain_jwt_token),
	path('', include(router.urls)),
	path('notes/tag/<slug>', TageViewSet.as_view({'get':'list',}), name='tagged'),
	path('notes/public/tag/<slug>', SherachPublicTag.as_view({'get':'list',}),name='sharedtag'),
	path('notes/search/', SearchNotesSet.as_view({'get':'list',}), name='searched'),
	path('notes/public/search/', SearchPublicNoteSet.as_view({'get':'list',}), name='sharedsearch'),
	path('notes/public/', Public.as_view({'get':'list',}),name='shared'),
	path('notes/<int:pk>/edit/',Update.as_view({'put': 'update'}),name='reload')

]