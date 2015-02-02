from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'work_manager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'tasksmanager.views.page'),
    url(r'^index$', 'tasksmanager.views.page'),
    url(r'^admin/', include(admin.site.urls)),
)
