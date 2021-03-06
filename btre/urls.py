"""btre URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('pages.urls')),
    path('listings/' , include('listings.urls')),
    path('contacts/' , include('contacts.urls')),
    path('accounts/' , include('accounts.urls')),# anything is accounts/ include accounts urls
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

# Admin Site Config
#admin.sites.AdminSite.site_header = 'BT Real Estate'
#admin.sites.AdminSite.site_header = '<img src="{% static 'img/logo.png%}" alt=""  class="brand_img" />'
#admin.sites.AdminSite.site_title = 'My site admin title'
#admin.sites.AdminSite.index_title = 'My site admin index'