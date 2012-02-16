import django.views.generic as gv
from django.http import HttpResponse, HttpResponseRedirect, Http404

from stargazer.demo.data import all_bricks

class RootV(gv.TemplateView):
    ''''''
    template_name = 'stargazer/pg/under_construction.html'
    

class IndexV(gv.TemplateView):
    ''''''
    template_name = 'stargazer/pg/index.html'
    
    def get_context_data(self):
        return {
            'brick_list': all_bricks
        }    
    
    
class DashboardV(gv.TemplateView):
    ''''''
    template_name = 'stargazer/pg/dashboard.html'       
    
    def get_context_data(self):
        return demo_context     