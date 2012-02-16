import django.views.generic as gv
from django.http import HttpResponse, HttpResponseRedirect, Http404

from stargazer.demo.data import all_bricks, context_data as demo_context

class RootV(gv.RedirectView):
    ''''''
    url = '/index/'
    

class IndexV(gv.TemplateView):
    ''''''
    template_name = 'stargazer/pg/index.html'
    
    def get_context_data(self):
        return {
            'brick_list': all_bricks
        }
        
        
class ExploreV(gv.TemplateView):
    ''''''
    template_name = 'stargazer/pg/explore.html'
    
    def get_context_data(self):
        return {
            'brick_list': all_bricks
        }        
    
    
class DashboardV(gv.TemplateView):
    ''''''
    template_name = 'stargazer/pg/dashboard.html'       
    
    def get_context_data(self):
        context = demo_context
        context.update({
            'brick_list': all_bricks[:6]                        
        });
        return context