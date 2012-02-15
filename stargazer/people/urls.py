from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
import views as v

urlpatterns = patterns('',    
    url(r'^v/(?P<username>[\w@\+\.-]+)/$', v.DetailV.as_view()),
)
