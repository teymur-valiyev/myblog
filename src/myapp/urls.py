from django.conf.urls import include, url

urlpatterns = (
    url(r'^$','myapp.views.about',name='about'),
)
