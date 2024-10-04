from django.urls import path
from . import views
from .views import *
from django.contrib import admin  
from django.conf import settings  
from django.conf.urls.static import static  

urlpatterns = [
    # path('test_session/',views.test_session,name="login"),
    path('api/LoginModelCreateView/',LoginModelCreateView.as_view(), name='LoginModelCreateView'),
    path('api/LoginView/',LoginView.as_view(), name='LoginView'),
    path('api/LogoutView/',LogoutView.as_view(), name='LogoutView'),
    path('api/MenuItemsList/',MenuItemsList.as_view(), name='MenuItemsView'),
    path('api/OrderItemsList/', OrderItemsList.as_view(), name='OrderItemsView'),
    path('api/CategoryItemsList/',CategoryItemsList.as_view(),name="Categoryitemsshow"),
    path('api/DeleteOrderIfNull/<int:pk>/', DeleteOrderIfNull.as_view(), name='DeleteOrderIfNull'),
    path('api/categoryFiltering/',CategoryFiltering.as_view(), name='categoryFiltering'),
    path('api/Update_menu/<int:id>/',Update_menu.as_view(), name='Update_menu'),
    path('api/Update_hide/<int:id>/',Update_hide.as_view(), name='Update_hide'),
    path('api/Category_update/<int:id>/',Category_update.as_view(), name='Category_update'),
    path('api/Food_order_updation/<int:id>/',Food_order_updation.as_view(), name='Food_order_updation'),
    path('api/Update_order_placing/<int:id>/',Update_order_placing.as_view(), name='Update_order_placing'),







]
if settings.DEBUG:  
  urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  