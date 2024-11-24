from django.urls import path
from .import views

app_name ="brands_app"

urlpatterns = [
    path('all/',views.all_brands_view, name='all_brands_view'),
    path('details/<int:brand_id>/',views.brand_detail_view, name='brand_detail_view'),
    path('new/',views.new_brand_view, name='new_brand_view'),
    path('update/<int:brand_id>/',views.update_brand_view, name='update_brand_view'),
    path('delete/<int:brand_id>/',views.brand_delete_view, name='brand_delete_view'),
]