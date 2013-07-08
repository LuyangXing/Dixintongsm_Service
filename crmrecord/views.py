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

from django.http import HttpResponse
from django.template import loader


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


def recordcreate(request):
    return render_to_response('recordcreate.html', context_instance=RequestContext(request))

@csrf_protect
def creater(request):
    qcddid = request.POST['qcddid']
    qcwwid = request.POST['qcwwid']
    qcstate = request.POST['qcstate']
    qccharger = request.POST['qccharger']
    qcdemand = request.POST['qcdemand']
    qcnotes = request.POST['qcnotes']
    record_add(qcddid,qcwwid,qcstate,qccharger,qcdemand,qcnotes)
    return render_to_response('record-creater.html', context_instance=RequestContext(request))

def record_add(qcddid,qcwwid,qcstate,qccharger,qcdemand,qcnotes):
    p = RecordList(cddid=qcddid,
                   cwwid=qcwwid,
                   cdatetime=datetime.datetime.now(),
                   cstate=qcstate,
                   ccharger=qccharger,
                   cdemand=qcdemand,
                   cnotes=qcnotes)
    p.save()


def recordpatch(request):
    ngword = NgWord.objects.get(pk=request.POST['id'])
    pass

@csrf_protect
def patcher(request):
    qcddid = request.POST['qcddid']
    qcwwid = request.POST['qcwwid']
    qcstate = request.POST['qcstate']
    qccharger = request.POST['qccharger']
    qcdemand = request.POST['qcdemand']
    qcnotes = request.POST['qcnotes']
    record_add(qcddid,qcwwid,qcstate,qccharger,qcdemand,qcnotes)
    return render_to_response('record-creater.html', context_instance=RequestContext(request))

def record_update(qcddid,qcwwid,qcstate,qccharger,qcdemand,qcnotes):
    ngword = NgWord.objects.get(pk=request.POST['id'])
    ngword.info = request.POST['info']
    ngword.name = request.POST['name']
    ngword.update_date = datetime.datetime.now()
    ngword.save()


def recordlist(request):
    state = request.GET.get('state')
    if state == 'pending':
        pass
    if state == 'complete':
        pass
    if state == 'all':
        pass

def orderlist(request):
    gcddid = request.POST['gcddid']
    print gcddid
    gcddid = gcddid.replace(" ", "")
    print gcddid
    rof_ddid = RecordList.objects.filter(cddid__contains=gcddid)
    try:
        if gcddid == '':
            return render_to_response('record-creater.html', context_instance=RequestContext(request))
        elif gcddid in rof_ddid[0].cddid:
            t = loader.get_template("record-patcher.html")
            c = RequestContext(request,{'rof_ddid': rof_ddid})
            return HttpResponse(t.render(c))
    except:
        return render_to_response('record-creater.html', context_instance=RequestContext(request))



