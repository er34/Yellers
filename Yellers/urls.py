from django.conf.urls import patterns, include, url
from accounts import views as acviews

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'accounts.views.entry', name='entry'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', acviews.login, name='login'),
    url(r'^logout/', acviews.logout, name='logout'),
    url(r'^registration/', acviews.registration, name='registration'),
)
