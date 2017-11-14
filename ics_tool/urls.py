from django.conf.urls import url, patterns
from django.contrib.auth import views as auth_views
from django.conf import settings

from . import views

app_name='ics_tool'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^donor$', views.add_donor, name='add_donor'),
    url(r'^search_donor$', views.search_donor, name='search_donor'),

]

if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
