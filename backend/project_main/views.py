from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
#from django.shortcuts import redirect


class PlanAView(LoginRequiredMixin, TemplateView):
    template_name = "plan_a/index.html"


#def redirect_view(request): #redirect view :D for the future
#    if not request.user.is_authenticated:
#        redir = 'login'
#    else:
#        redir = 'inicio'
#    return redirect(redir)
