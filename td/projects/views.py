from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.core.management import call_command
from .models import Project, UpdateCheck

def home(request):
    """
    Calls database update function and renders the table
    """
    project = Project.objects.all()  
    last_updated = UpdateCheck.objects.order_by('last_update').last()
    return render(request, "projects/list.html",{          
        'project': project,  
        'last_updated': last_updated,                       
    })


def force_update(request):
    '''
    Forces database to rescan api and update
    '''
    td_force_update = call_command('forceupdate')
    return HttpResponseRedirect(reverse("home"))
