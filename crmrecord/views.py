# Create your views here.

from django.shortcuts import render_to_response
from django.contrib.auth import authenticate,login,logout

from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required



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
    if dingdanid == "dd123456" or wangwangid == "ww123456":
        return render_to_response('record-patcher.html', context_instance=RequestContext(request))
    else:
        return render_to_response('record-creater.html', context_instance=RequestContext(request))

def record_mid_creater(request):
    pass

def record_mid_patcher(request):
    pass

