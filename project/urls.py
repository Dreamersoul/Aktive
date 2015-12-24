"""letsroll URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
from project import settings
from main.views import profile_detail, all_activities, activities, categories, register, activitiesFromCategory

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^user/', profile_detail),
    url(r'^login/', obtain_auth_token),
    url(r'^activities/(?P<category>\w+)/$', activitiesFromCategory),
    url(r'^all_activities', all_activities),
    url(r'^activities', activities),
    url(r'^categories', categories),
    url(r'^register', register),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
