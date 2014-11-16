from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.generic.base import TemplateView
from users.forms import LoginForm
from users.views import LoginView

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
                       url(r'^login$', LoginView.as_view(), name='login'),
                       url(r'^register$', 'users.views.register', name='register'),

                       url(r'^$', 'shopCatalog.views.index', name='index'),

                       url(r'^add$', 'shopCatalog.views.addGood', name='add_good'),

                       url(r'^catalog$', 'shopCatalog.views.render_catalog', name='catalog'),

                       url(r'^good/(?P<good_id>\d+)/$', 'shopCatalog.views.render_good', name='good_page'),

                       url(r'^watched/$', "users.views.render_watched", name='watched_goods'),

                       url(r'^good/(?P<good_id>\d+)/add$', 'shopCatalog.views.add_to_cart', name='add_to_cart'),

                       url(r'^cart/$', "shopCatalog.views.render_cart", name='cart'),

                       url(r'^cart/delete/(?P<good_id>\d+)$', "shopCatalog.views.delete_from_cart",
                           name='delete_from_cart'),

                       url(r'^contacts/$', TemplateView.as_view(template_name="contacts.html"), name='contacts'),

                       url(r'^site/', include('admin.urls', namespace='site_admin')),
)
