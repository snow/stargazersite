import django.views.generic as gv
from django.http import HttpResponse, HttpResponseRedirect, Http404

from stargazer.demo.data import context_data as demo_context

class StreamV(gv.TemplateView):
    ''''''
    template_name = 'stargazer/pg/under_construction.html'
    
    
class DetailV(gv.TemplateView):
    ''''''
    template_name = 'stargazer/pg/place_detail.html'
    
    def get_context_data(self, username):
        return demo_context    