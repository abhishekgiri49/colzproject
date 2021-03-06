from django.contrib import admin
from django.urls import include
from django.urls import path
from blog import burl
from django.conf.urls.static import static
from django.conf import settings
from account import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(burl)),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('account/', include('account.urls')),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


