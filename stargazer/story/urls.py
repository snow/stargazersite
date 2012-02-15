from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
import views as v

urlpatterns = patterns('',
    url(r'^tagged/(?P<tag_name>.+)/$', v.StreamV.as_view()),
    url(r'^v/(?P<id_str>\w+)/', v.DetailV.as_view()),
)