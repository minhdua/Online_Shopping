from django.urls import path
from django.urls import include, path
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include(('apps.authentication.urls','authentication'), namespace='authentication')),
    path('cals/', include(('apps.categories_and_labels.urls','categories_and_labels'), namespace='categories_and_labels')),
    path('shops/',include(('apps.shops.urls','shop'),namespace='shops')),
    path('products/',include(('apps.products.urls','products'),namespace='products')),
    path('bills/',include(('apps.bills.urls','bills'),namespace='bills')),
    #path('carts/',include(('apps.carts.urls','carts'),namespace='carts')),

]
