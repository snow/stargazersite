import django.views.generic as gv
from django.http import HttpResponse, HttpResponseRedirect, Http404


class StreamV(gv.TemplateView):
    ''''''
    template_name = 'stargazer/pg/under_construction.html'
    
    
class DetailV(gv.TemplateView):
    ''''''
    template_name = 'stargazer/pg/under_construction.html'    