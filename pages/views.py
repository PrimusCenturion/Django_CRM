from django.views.generic import TemplateView
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if "TEST" in self.request.session:
            context['TEST'] = self.request.session['TEST']
        return context

    # def get(self, request, *args, **kwargs):
    #     if "TEST" in request.session:
    #         request.session['TEST'].append("VISIT")
    #         request.session.modified = True
    #     else:
    #         pass
    #     return super().get(request, *args, **kwargs)


    
def cookie_preferences(request):
        
        if request.method == "POST":
            if request.POST.get('accepted') == 'true':
                if "TEST" in request.session:
                    request.session['TEST'].append("VISIT")
                else:
                    request.session['TEST'] = ["VISIT"]
                request.session.modified = True
            return HttpResponse(status=200)
        
        else:
            return HttpResponseRedirect(reverse_lazy("home"))