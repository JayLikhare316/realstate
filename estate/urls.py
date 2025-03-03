from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('bloggrid', views.bloggrid, name='bloggrid'),
    path('propertygrid', views.propertygrid, name='propertygrid'),
    path('propertysingle', views.propertysingle, name='propertysingle'),
    path('blogsingle', views.blogsingle, name='blogsingle'),
    path('agentsgrid', views.agentsgrid, name='agentsgrid'),
    path('agentsingle', views.agentsingle, name='agentsingle'),

]
