from django.urls import include, path
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    path('', include('fs.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path(r'^__debug__/', include(debug_toolbar.urls)),
    ]


# NEED TO ADD TEMPLATES FOR INDEX AND ACCOUNTS
