from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('', include('fs.urls')),
    path('login/', include('fs.urls')),
    path('admin/', admin.site.urls),
]



# NEED TO ADD TEMPLATES FOR INDEX AND ACCOUNTS
