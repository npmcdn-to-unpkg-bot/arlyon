from django.template import loader
from django.http import HttpResponse
from django.shortcuts import redirect

def profile(request):
    if request.user.is_authenticated():
        template = loader.get_template('generic/profile.html')
        context = {
        }
        return HttpResponse(template.render(context, request))
    else:
        return redirect('/accounts/login')
