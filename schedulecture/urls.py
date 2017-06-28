from django.conf.urls import url
from django.contrib import admin

from institute import views as inst_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^center/(?P<id>\d+)/calendar/$', inst_views.center_calendar),
    url(r'^center/(?P<id>\d+)/save/$', inst_views.save_center_calendar),
]
