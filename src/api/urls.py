from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter

from . import views

from .views import NoteViewSet,TageViewSet, SearchNotesSet,\
	SearchPublicNoteSet,SherachPublicTag,Public,Register

app_name = 'api'

router = DefaultRouter(trailing_slash=False)

router.register(r'notes', NoteViewSet)
router.register(r'register',Register,base_name='User')


# eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6InBhbGFkaW5rdW1wYW4yMDE2QHlhbmRleC5ydSIsImV4cCI6MTYzNzkxOTY0MSwiZW1haWwiOiJwYWxhZGlua3VtcGFuMjAxNkB5YW5kZXgucnUifQ.nIlxQE2eqbpnMpwjZKNCxjZ84gdgE5__nWwdDTQarNM
#eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6InBhbGFkaW5rdW1wYW4yMDE2QHlhbmRleC5ydSIsImV4cCI6MTYzNzkxNjc5MywiZW1haWwiOiJwYWxhZGlua3VtcGFuMjAxNkB5YW5kZXgucnUifQ.GMJN1PMIE7qjJF4AV0wRSiZ_iz7pprrhqoXapSEekYg
# curl -X GET http://127.0.0.1:8000/api/notes/tag/0 -H "Authorization: Token nIlxQE2eqbpnMpwjZKNCxjZ84gdgE5__nWwdDTQarNM"
#curl -H "Authorization: JWT nIlxQE2eqbpnMpwjZKNCxjZ84gdgE5__nWwdDTQarNM" http://127.0.0.1:8000/api/notes/tag/0
# curl -X GET -H "Authorization: Token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6InNreWxhcmdyZXlwcm9AeWFuZGV4LnJ1IiwiZXhwIjoxNjM3OTIxNzI1LCJlbWFpbCI6InNreWxhcmdyZXlwcm9AeWFuZGV4LnJ1In0.ZPTRU7TTFDqvllv7ZCHtwVo1HDQXk3D-s33l59VHfMU Content-Type: application/json"  http://127.0.0.1:8000/api/notes/tag/0
# curl -X GET http://127.0.0.1:8000/api/notes/tag/0 -H 'Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b'
# curl -X GET http://127.0.0.1:8000/api/notes/public/ -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6InNreWxhcmdyZXlwcm9AeWFuZGV4LnJ1IiwiZXhwIjoxNjM3OTIyMzM2LCJlbWFpbCI6InNreWxhcmdyZXlwcm9AeWFuZGV4LnJ1In0.6RqMPWfPbUV31NjEntTtlt4aMNbiNP6IIdr5J0DrtK4'
# curl -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6InNreWxhcmdyZXlwcm9AeWFuZGV4LnJ1IiwiZXhwIjoxNjM3OTI0NTQ2LCJlbWFpbCI6InNreWxhcmdyZXlwcm9AeWFuZGV4LnJ1In0.PbW0uWl1CSLzBJWbBw6QlEnrZa8zVOqxxlJfNMTxnpU" http://127.0.0.1:8000/api/notes/public/
# curl -X GET http://127.0.0.1:8000/api/notes/public/ -H 'Authorization: Token PbW0uWl1CSLzBJWbBw6QlEnrZa8zVOqxxlJfNMTxnpU'


"""
TOKEN=$(curl -s -X POST -H 'Accept: application/json' -H 'Content-Type: application/json' --data '{"username":"{username}","password":"{password}","rememberMe":false}' http://127.0.0.1:8000/api/jwt-auth/ | jq -r '.id_token')
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"email":"skylargreypro@yandex.ru","password":"26"}' \
  http://localhost:8000/api/jwt-auth/


curl --header "Accept: application/json" \
  --request POST \
  --data '{"email":"skylargreypro@yandex.ru","password":"26"}' \
  http://localhost:8000/api/jwt-auth/

"""
urlpatterns = [
	path('jwt-auth/', obtain_jwt_token),
	path('', include(router.urls)),
	path('notes/tag/<slug>', TageViewSet.as_view({'get':'list',}), name='tagged'),
	path('notes/public/tag/<slug>', SherachPublicTag.as_view({'get':'list',}), name='sharedtag'),
	path('notes/search/', SearchNotesSet.as_view({'get':'list',}), name='searched'),
	path('notes/public/search/', SearchPublicNoteSet.as_view({'get':'list',}), name='sharedsearch'),
	path('notes/public/', Public.as_view({'get':'list',}), name='shared'),
	path('notes/<int:pk>/edit/', NoteViewSet.as_view({'put': 'update'}), name='reload'),
	path('notes/new/', NoteViewSet.as_view({'post': 'create'}), name='create'),
	path('notes/delete/<int:pk>/', NoteViewSet.as_view({'delete': 'destroy'}), name='del'),
	path('notes/', NoteViewSet.as_view({'get': 'list'}), name='note-list')


]