from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from crmrecord.views import index, dashboard
from crmrecord.views import login_v, logout_v


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bjdxtmall.views.home', name='home'),
    # url(r'^bjdxtmall/', include('bjdxtmall.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^index$', index),
    (r'^dashboard$', dashboard),
    (r'^tracking$', index),
    (r'^record$', index),
    url(r'^login$', view=login_v, name="login_v"),
    url(r'^logout$', view=logout_v, name="logout_v"),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

