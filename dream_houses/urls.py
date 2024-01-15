# defining url patterns for dream_houses
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views
app_name = 'dream_houses'

urlpatterns = [
	# Home page name
	path('', views.index, name ='index'),
	path('dashboard/', views.dashboard, name = 'dashboard'),
	# Page for adding a new property
	path('new_property/', views.new_property, name ='new_property'),
	#Detail page for editing an entry
	path('edit_property/<int:property_id>/', views.edit_property, name = 'edit_property'),
	path('logout/', views.logout_view, name = 'logout')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)