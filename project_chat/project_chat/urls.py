from django.contrib import admin
from django.urls import path, include

from django.views.generic.base import TemplateView

# TemplateView should be used when you want to present some information
# in a html page.Showing ‘about us’ like pages which are static and hardly needs any context


urlpatterns = [
    path('admin/', admin.site.urls),          # admin view
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')), # The auth app we’ve now included provides us with
    # several authentication views and URLs for handling login, logout, and password management.
    path('chat/', include('chat.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

]