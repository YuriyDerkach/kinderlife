from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webapp.urls')),
    path('crm/', include('webapp.urls')),
    path('storage', include('webapp.urls')),
    path('login', include('webapp.urls')),
]
