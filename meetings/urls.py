from django.urls import path

from . import views

urlpatterns = [
    path('<int:m_id>', views.detail, name="detail"),
    path('room/<int:r_id>', views.detail_room, name="detail_room"),
    path('rooms', views.rooms_list, name="rooms"),
    path('new', views.new, name="new"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('edit_room/<int:id>', views.edit_room, name="edit_room"),
    path('delete/<int:id>', views.delete, name="delete")
]
