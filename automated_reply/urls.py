from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def default_view(request):
    return HttpResponse("Hello World!")

urlpatterns = [
    path("", default_view),
    path('admin/', admin.site.urls),
    path('api/v1/', include('apis.urls')),
    path('api/v1/scheduler/', include('scheduler.urls'))
]
