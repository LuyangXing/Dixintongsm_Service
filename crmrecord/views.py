# coding=utf-8
# Create your views here.

from django.shortcuts import render_to_response
from django.contrib.auth import authenticate,login,logout

from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from crmrecord.models import RecordList
import datetime



def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))

@csrf_protect
def login_v(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return render_to_response('index.html', context_instance=RequestContext(request))
            # Redirect to a success page.
        else:
            return render_to_response('index.html', context_instance=RequestContext(request))
            # Return a 'disabled account' error message
    else:
        return render_to_response('index.html', context_instance=RequestContext(request))
        # Return an 'invalid login' error message.


def logout_v(request):
    logout(request)
    return render_to_response('index.html', context_instance=RequestContext(request))

@login_required(login_url='/index')
def dashboard(request):
    return render_to_response('dashboard.html', context_instance=RequestContext(request))

@login_required(login_url='/index')
def record_seacher(request):
    return render_to_response('record-seacher.html', context_instance=RequestContext(request))

@csrf_protect
def record_mid_searcher(request):
    dingdanid = request.POST['dingdanid']
    wangwangid = request.POST['wangwangid']
    if dingdanid == RecordList.objects.filter(cddid=dingdanid) or RecordList.objects.filter(cwwid=wangwangid):
        return render_to_response('record-patcher.html', context_instance=RequestContext(request))
    else:
        return render_to_response('record-creater.html', context_instance=RequestContext(request))

@csrf_protect
def record_mid_creater(request):
    qcddid = request.POST['qcddid']
    qcwwid = request.POST['qcwwid']
    qcstate = request.POST['qcstate']
    qccharger = request.POST['qccharger']
    qcdemand = request.POST['qcdemand']
    qcnotes = request.POST['qcnotes']

    p = RecordList(cddid=qcddid,
                   cwwid=qcwwid,
                   cdatetime=datetime.datetime.now(),
                   cstate=qcstate,
                   ccharger=qccharger,
                   cdemand=qcdemand,
                   cnotes=qcnotes)
    p.save()
    return render_to_response('record-creater.html', context_instance=RequestContext(request))

# def record_mid_patcher(request):
#     pass

