from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('user/', include('fs.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]



# NEED TO ADD TEMPLATES FOR INDEX AND ACCOUNTS
