from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
import views as v

urlpatterns = patterns('',
    url(r'^$', v.RootV.as_view()),
    url(r'^index/$', v.IndexV.as_view()),
    url(r'^explore/$', v.ExploreV.as_view()),
    url(r'^dashboard/$', v.DashboardV.as_view()),
    
    url(r'^people/', include('stargazer.people.urls')),
    
    url(r'^journeys/', include('stargazer.journey.urls')),
    
    url(r'^stories/', include('stargazer.story.urls')),
    
    url(r'^places/', include('stargazer.place.urls')),
)
