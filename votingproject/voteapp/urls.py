from django.conf.urls import url
from . import views

app_name="voteapp"

urlpatterns = [
    url(r'^$',views.votes, name="votes"),
    url(r'^malepresenter/$', views.males, name="males"),
    url(r'^femalepresenter/$', views.females, name="females"),
]