from django.urls import path
from django.conf.urls import url
from .views import (
    CategoryListCreate,CategoryRUD,LabelListCreate,LabelRUD)

appname = 'categoriesandlabels'
urlpatterns = [
    # List and create category
    path('categories/',CategoryListCreate.as_view()),
    # Detail category
    path('categories/<int:pk>/',CategoryRUD.as_view()),
    #list labels inside specific category
    path('labels/',LabelListCreate.as_view()),
    # Detail label
    path('labels/<int:pk>/',LabelRUD.as_view()),
    # List products in a specific label

]
