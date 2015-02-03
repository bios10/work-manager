from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'work_manager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^$', 'tasksmanager.views.index', name="public_index"),
    url(r'^connection$', 'tasksmanager.views.connection', name="public_connection"),
    url(r'^project-detail-(?P<pk>\d+)$', 'tasksmanager.views.project_detail', name="project_detail"),
    url(r'^create-developer$', 'tasksmanager.views.create_developer', name="create_developer"),
    url(r'^create-supervisor$', 'tasksmanager.views.create_supervisor', name="create_supervisor"),
    url(r'^admin/', include(admin.site.urls)),
)
