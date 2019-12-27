from django.urls import path
from django.urls import include, path
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include(('apps.authentication.urls','authentication'), namespace='authentication')),
    #path('categories/', include(('apps.categories.urls','categories'), namespace='category')),

]
