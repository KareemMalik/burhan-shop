from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    # ===== Home / Auth (pages) =====
    path('', views.show_main, name='show_main'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_user, name='logout'),

    # ===== Product pages (server-rendered) =====
    path('create-product/', views.create_product, name='create_product'),
    path('product/<uuid:id>/', views.show_product, name='show_product'),
    path('product/<uuid:id>/edit', views.edit_product, name='edit_product'),
    path('product/<uuid:id>/delete', views.delete_product, name='delete_product'),

    # ===== Data endpoints (JSON/XML) =====
    path('json/', views.show_json, name='show_json'),
    path('json/<uuid:id>/', views.show_json_by_id, name='show_json_by_id'),
    path('xml/', views.show_xml, name='show_xml'),
    path('xml/<uuid:id>/', views.show_xml_by_id, name='show_xml_by_id'),

    # ===== AJAX endpoints (no full page reload) =====
    # Create via AJAX (modal)
    path('create-product-ajax/', views.add_product_ajax, name='add_product_ajax'),
    # Update/Delete via AJAX
    path('api/products/<uuid:id>/update/', views.update_product_ajax, name='api_update_product'),
    path('api/products/<uuid:id>/delete/', views.delete_product_ajax, name='api_delete_product'),

    # Auth via AJAX
    path('api/auth/login/', views.api_login, name='api_login'),
    path('api/auth/register/', views.api_register, name='api_register'),
    path('api/auth/logout/', views.api_logout, name='api_logout'),
]
