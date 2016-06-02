from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('account.urls')),
    url('social-auth/', include('social.apps.django_app.urls', namespace='social')),
    url(r'^images/', include("images.urls", namespace="images")),
]
