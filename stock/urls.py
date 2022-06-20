# from django.urls import path 
# urlpatterns = [ 
# ]
from django.urls import path
from stock.views import add_item, delete_item, index, update_item, lista_escala
urlpatterns = [
    path('', index, name='index'),
    path('add-item', add_item, name='add-item'),
    path('update-item/<int:item_id>', update_item, name='update-item'),
    path('delete-item/<int:item_id>', delete_item, name='delete-item'),
    path('lista-escala/<int:item_id>', lista_escala, name='lista-escala'),
]