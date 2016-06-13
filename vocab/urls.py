from django.conf.urls import url, include
from . import views

terms = [
    url(r'^edit/$', views.EditTermView.as_view(), name='edit_term'),
    url(r'^list/$', views.TermListCreateView.as_view(), name='list_create'),
    url(r'^detail/(?P<pk>[0-9])/$', views.TermDetailView.as_view(), name='detail'),
]

relationships = [
    url(r'^list/$', views.RelationshipListCreateView.as_view(), name='list_create'),
    url(r'^detail/(?P<pk>[0-9])/$', views.RelationshipDetailView.as_view(), name='detail'),
]

urlpatterns = [
    url(r'^$', views.MainPageView.as_view(), name='main_page'),
    url(r'^graph/$', views.VocabGraphView.as_view(), name='vocab_graph'),
    url(r'^terms/', include(terms, namespace='terms')),
    url(r'^relationships/', include(relationships, namespace='relationships')),
]
