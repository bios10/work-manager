from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'work_manager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'tasksmanager.views.index', name="public_index"),
    url(r'^connection$', 'tasksmanager.views.connection', name="public_connection"),
    url(r'^admin/', include(admin.site.urls)),
)
