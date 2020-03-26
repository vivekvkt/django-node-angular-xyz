from django.urls import path
from .views import (
    index,
    item,
    detailView,
    createItem,
    updateItem,
    deleteItem,
    IndexClassBasedView,
    DetailClassBasedView,
    CreateClassBasedView
)



app_name = 'food'
urlpatterns = [
    #path('',index, name='index'),
    path('item/',item, name='item'),
    #path('<int:item_id>/',detailView, name='detail'),
    #path('addItem/',createItem, name='addItem'),
    path('updateItem/<int:id>/',updateItem, name='updateItem'),
    path('deleteItem/<int:id>/',deleteItem, name='deleteItem'),
    path('',IndexClassBasedView.as_view(), name='index'),
    path('<int:pk>/',DetailClassBasedView.as_view(), name='detail'),
    path('addItem/',CreateClassBasedView.as_view(), name='addItem')
]