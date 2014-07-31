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
    url(r'^doregister/', acviews.doregister, name='doregister'),
    url(r'^mailverify/(?P<username>\w+)/(?P<mailkey>\w+)/', acviews.mailverify, name='mailverify'),
    url(r'^isUserExists/(?P<username>\w+)/', acviews.isUserExists, name='isUserExists'),
    url(r'^account/', acviews.account, name='account'),
)

urlpatterns += patterns('',
    url(r'^captcha/', include('captcha.urls')),
)