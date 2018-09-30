from django.conf.urls import url
from . import views
app_name="loginapp"

urlpatterns = [
    url(r'^$', views.login_user, name="login_user"),
]