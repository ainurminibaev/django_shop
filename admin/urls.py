from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'OnlineShop.views.home', name='home'),
    # url(r'^OnlineShop/', include('OnlineShop.foo.urls')),

    url(r'^categories$', 'admin.views.render_manage_category', name='manage_category'),
)
