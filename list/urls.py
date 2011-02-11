from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^grocery/$', 'list.views.index', name="grocery_list"),
    url(r'^grocery/delete/(?P<id>\d+)/$', 'list.views.groceryDelete', name='grocery_delete'),
    url(r'^grocery/ajaxdelete/$', 'list.views.groceryAjaxDelete', name='grocery_Ajaxdelete'),
    url(r'^grocery/create/$', 'list.views.groceryCreate', name="grocery_create"),
    url(r'^grocery/edit/(?P<user>[-\w]+)/(?P<slug>[-\w]+)/$', 'list.views.groceryCreate', name='grocery_edit'),
    url(r'^grocery/(?P<user>[-\w]+)/(?P<slug>[-\w]+)/$', 'list.views.groceryShow', name='grocery_show'),
    url(r'^grocery/print/(?P<user>[-\w]+)/(?P<slug>[-\w]+)/$', 'list.views.groceryShow', {'template_name':'list/grocery_print.html',}, name='grocery_print'),
    url(r'^grocery/grocery-ajax/$', 'list.views.groceryProfile', name="grocery_profile"),
   )