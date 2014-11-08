from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.generic.base import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'OnlineShop.views.home', name='home'),
                       # url(r'^OnlineShop/', include('OnlineShop.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),

                       url(r'^logout$', 'users.views.sign_out', name='logout'),
                       url(r'^login$', 'users.views.sign_in', name='login'),
                       url(r'^register$', 'users.views.register', name='register'),

                       url(r'^$', 'shopCatalog.views.index', name='index'),

                       url(r'^add$', 'shopCatalog.views.addGood', name='add_good'),

                       url(r'^catalog$', 'shopCatalog.views.render_catalog', name='catalog'),

                       url(r'^good/(?P<good_id>\d+)/$', 'shopCatalog.views.render_good', name='good_page'),
                       url(r'^watched/$', "users.views.render_watched",  name='watched_goods'),

                       url(r'^site/', include('admin.urls', namespace='site_admin')),
)
