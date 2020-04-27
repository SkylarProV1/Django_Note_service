"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
	# Handle the root url.
	path('', RedirectView.as_view(url='notes/'), name='index'),
	# Accounts app
	path('accounts/', include('accounts.urls', namespace='accounts')),
	# Notes app
	path('notes/', include('notes.urls', namespace='notes')),
    path('api/', include('api.urls', namespace='api')),
    
]#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

