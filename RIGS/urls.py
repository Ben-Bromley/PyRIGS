from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from RIGS import views

from PyRIGS.decorators import permission_required_with_403

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'PyRIGS.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^closemodal/$', views.CloseModal.as_view(), name='closemodal'),

                       url('^user/login/$', 'RIGS.views.login', name='login'),

                       # People
                       url(r'^people/$', permission_required_with_403('RIGS.view_person')(views.PersonIndex.as_view()),
                           name='person_list'),
                       url(r'^people/(?P<pk>\d+)/$',
                           permission_required_with_403('RIGS.view_person')(views.PersonDetail.as_view()),
                           name='person_detail'),
                       url(r'^people/add/$',
                           permission_required_with_403('RIGS.add_person')(views.PersonCreate.as_view()),
                           name='person_add'),
                       url(r'^people/(?P<pk>\d+)/edit/$',
                           permission_required_with_403('RIGS.change_person')(views.PersonUpdate.as_view()),
                           name='person_update'),
)

