from django.contrib import admin
from django.urls import path, include


from django.conf.urls import handler404
from members.views import custom_404 

urlpatterns = [
    path('', include('members.urls')),
    path('admin/', admin.site.urls),
]

handler404 = 'members.views.custom_404'