from django.template import loader
from django.http import HttpResponse
from django.shortcuts import redirect


def profile(request):
    if request.user.is_authenticated():
        template = loader.get_template('generic/profile.html')
        is_family = request.user.groups.filter(name='Family').exists()
        context = {
            "is_family": is_family
        }
        return HttpResponse(template.render(context, request))
    else:
        return redirect('/accounts/login')


def landing(request):
    template = loader.get_template('generic/landing.html')
    is_family = request.user.groups.filter(name='Family').exists()
    context = {
        "is_family": is_family
    }
    return HttpResponse(template.render(context, request))
