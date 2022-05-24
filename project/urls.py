
from django.contrib import admin
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls',namespace='accounts')),
    path('contact',include('contact.urls',namespace='contact')),
    path('gallery',include('gallery.urls',namespace='gallery')),
] 
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 