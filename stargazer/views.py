import django.views.generic as gv
from django.http import HttpResponse, HttpResponseRedirect, Http404

from stargazer.demo.data import context_data as demo_context

class RootV(gv.TemplateView):
    ''''''
    template_name = 'stargazer/pg/under_construction.html'
    

class IndexV(gv.TemplateView):
    ''''''
    template_name = 'stargazer/pg/index.html'
    
    def get_context_data(self, username):
        return demo_context    
    
    
class DashboardV(gv.TemplateView):
    ''''''
    template_name = 'stargazer/pg/dashboard.html'       
    
    def get_context_data(self, username):
        return demo_context     