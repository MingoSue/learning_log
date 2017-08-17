from django.conf.urls import patterns, url
from django.contrib.auth.views import login
from . import views

# Uncomment the next two lines to enable the admin:
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'learning_log.views.home', name='home'),
    # url(r'^learning_log/', include('learning_log.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^login/$', login, {'template_name': 'users/login.html'},
        name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^register/$', views.register, name='register'),

)