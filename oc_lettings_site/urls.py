# from django.conf.urls import handler404, handler500
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
    path("", include("lettings.urls")),
    path("", include("profiles.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if the app is deployed
urlpatterns += staticfiles_urlpatterns()


handler500 = "home.views.custom_500"
handler404 = "home.views.custom_404"
