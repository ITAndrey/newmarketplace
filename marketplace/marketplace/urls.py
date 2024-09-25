from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from mainpage.views import index

urlpatterns = [
    path('', index, name='MainPage'),
    path('admin/', admin.site.urls),
]
