from django.conf.urls import url
from . import views

app_name = 'dashapp'

urlpatterns = [
    #/dashboard/
    url(r'^$', views.TeamList.as_view(), name="dashboard"),
    #/dashboard/female_presenters
    url(r'^female_presenters/$', views.FemaleList.as_view(), name="female_presenters"),
    url(r'^male_presenters/$', views.MaleList.as_view(), name="male_presenters"),
    url(r'^top_teams/$', views.ToptemsDetails.as_view(), name="top_teams"),
    url(r'^top_females/$', views.TopFemales.as_view(), name="top_females"),
    url(r'^top_males/$', views.TopMales.as_view(), name="top_males"),
    #/dashboard/create_team
    url(r'create_team/$', views.CreateTeam.as_view(), name='create_team'),
    url(r'add_female/$', views.AddFemale.as_view(), name='add_female'),
    url(r'add_male/$', views.AddMale.as_view(), name='add_male'),
    #/dashboard/team_pk
    url(r'^(?P<pk>[0-9]+)/$',views.TeamDetails.as_view(),name="team_details"),
    url(r'^(?P<team_id>[0-9]+)/add_member/$',views.add_member,name="add_member"),
    url(r'register/$', views.UserFormView.as_view(), name='register'),
    
]