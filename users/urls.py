# defining url patterns for dream_houses
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from . import views
app_name = 'users'

urlpatterns = [
	# Home page name
	path('', include('django.contrib.auth.urls')),	
	# Registration page
	path('register/', views.register, name = 'register'),
]
