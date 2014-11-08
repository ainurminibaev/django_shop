from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'OnlineShop.views.home', name='home'),
    # url(r'^OnlineShop/', include('OnlineShop.foo.urls')),

    url(r'^$', 'shopCatalog.views.index', name='index'),

    url(r'^add$', 'shopCatalog.views.addGood', name='add_good'),

    url(r'^catalog$', 'shopCatalog.views.render_catalog', name='catalog'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
     url(r'^site/', include('admin.urls', namespace='site_admin')),
)
