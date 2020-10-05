from django.shortcuts import render
import json
from django.http import HttpResponseRedirect, HttpRequest, request, HttpResponse

from django.urls import reverse_lazy
from django.http import HttpResponse, Http404

from userprofile.models import Profile
from django.contrib.auth.models import User 

from connected_kits.models import Kit, Button



def control(request, user_pk, kit_pk):
    try:
        user = User.objects.get(pk=user_pk)
        kit = Kit.objects.get(pk=kit_pk)
    except:
        raise Http404()
    status = {}
    buttons = Button.objects.filter(user=user, kit=kit)
    for button in buttons:
        status[button.name] = button.status

    json_str = json.dumps(status)

    return HttpResponse(json_str, content_type='text/plain')
  

    