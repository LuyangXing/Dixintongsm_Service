# coding=utf-8
# Create your views here.

from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout

from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from crmrecord.models import RecordList
import datetime

from django.http import HttpResponse
from django.http import HttpResponseRedirect
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
    OrderNo = request.POST['OrderNo']
    OrderNo = OrderNo.replace(" ", "")
    Authors = request.POST['Authors']
    ProblemSummary = request.POST['ProblemSummary']
    ProblemDescription = request.POST['ProblemDescription']
    EmergencyTreatment = request.POST['EmergencyTreatment']
    CallProcessing = request.POST['CallProcessing']
    State = request.POST['State']
    record_add(OrderNo, Authors, ProblemSummary, ProblemDescription, EmergencyTreatment,CallProcessing, State)
    return render_to_response('recordcreate.html', context_instance=RequestContext(request))

def record_add(OrderNo, Authors, ProblemSummary, ProblemDescription, EmergencyTreatment, CallProcessing, State):
    p = RecordList(OrderNo=OrderNo,
                   Authors=Authors,
                   ProblemSummary=ProblemSummary,
                   ProblemDescription=ProblemDescription,
                   DateTime=datetime.datetime.now(),
                   EmergencyTreatment=EmergencyTreatment,
                   CallProcessing=CallProcessing,
                   State=State,
                   DateTime2=datetime.datetime.now())
    p.save()

@login_required(login_url='/index')
def recordlist(request):
    state = request.GET.get('state')
    if state == 'complete':
        dbresults = RecordList.objects.filter(State=1)
        t = loader.get_template("recordlist.html")
        c = RequestContext(request,{'dbresults': dbresults})
        return HttpResponse(t.render(c))
    elif state == 'all':
        dbresults = RecordList.objects.all()
        t = loader.get_template("recordlist.html")
        c = RequestContext(request,{'dbresults': dbresults})
        return HttpResponse(t.render(c))
    else:
        dbresults = RecordList.objects.filter(State=0)
        t = loader.get_template("recordlist.html")
        c = RequestContext(request,{'dbresults': dbresults})
        return HttpResponse(t.render(c))

@login_required(login_url='/index')
def orderlist(request):
    OrderNo = request.GET.get('orderno')
    dbresults = RecordList.objects.filter(OrderNo=OrderNo)
    t = loader.get_template("orderlist.html")
    c = RequestContext(request,{'dbresults': dbresults})
    return HttpResponse(t.render(c))

def recordpatch(request):
    servicecode = request.GET.get('servicecode')
    t = loader.get_template("recordpatch.html")
    c = RequestContext(request,{'servicecode': servicecode})
    return HttpResponse(t.render(c))

@csrf_protect
def patcher(request):
    ServiceCode = request.POST['ServiceCode']
    State = request.POST['State']
    Head = request.POST['Head']
    ProcessResultsSummary = request.POST['ProcessResultsSummary']
    ProcessResultsDescription = request.POST['ProcessResultsDescription']
    record_update(ServiceCode, State, Head, ProcessResultsSummary, ProcessResultsDescription)
    return HttpResponseRedirect('recordlist')

def record_update(servicecode, State, Head, ProcessResultsSummary, ProcessResultsDescription):
    ServiceOrder = RecordList.objects.get(ServiceCode=servicecode)
    ServiceOrder.State=State
    ServiceOrder.DateTime2=datetime.datetime.now()
    ServiceOrder.Head=Head
    ServiceOrder.ProcessResultsSummary=ProcessResultsSummary
    ServiceOrder.ProcessResultsDescription=ProcessResultsDescription
    ServiceOrder.save()

def deleter(request):
    servicecode = request.GET.get('servicecode')
    p = RecordList.objects.get(ServiceCode=servicecode)
    p.delete()
    return HttpResponseRedirect('recordlist')