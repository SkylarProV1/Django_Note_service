from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib.auth import views as auth_views
from .views import RegisterView,Activate

app_name = 'accounts'

urlpatterns = [
	path('login/', auth_views.login, name='login'),
	path('logout/', auth_views.logout, {"next_page" : reverse_lazy('accounts:login')},
		name='logout'),
	path('register/', RegisterView.as_view(), name='register'),
	path('activate/<uidb64>/<token>', Activate.as_view(), name='activates'),
] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


