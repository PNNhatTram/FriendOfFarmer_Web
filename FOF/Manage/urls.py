from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name="index"),
<<<<<<< HEAD
    path('search', views.search, name='search'),
    path('manage/', views.manage, name='manage'),
    path('manage', views.home, name="manage"),
    path('logins', views.logins, name='logins'),
    path('Logout_page', views.Logout_page, name='Logout_page'),
    path('signup', views.signup, name='signup'),
    path('userin4', views.userin4, name='userin4'),
    path('create', views.m_form, name="create"),
    path('maker', views.maker, name="maker"),
    path('contact', views.contact, name="contact"),
    path('maker_sell/', views.maker_sell, name="maker_sell"),
=======
    path('login/', views.login, name = 'login'),
   
    
    path('manage/', views.manage, name='manage'),   
    path('create', views.m_form, name="create"),
>>>>>>> 83649d5c415e276eb467f4fc3808f4d13b3cf561
    path('create/land', views.land_form, name="land"),
    path('create/plant', views.plant_form, name="plant"),
    path('api/get-season-info/<int:season_id>/', views.get_season_info, name='get_season_info'),
    path('api/get-land-by-season/<int:season_id>/', views.get_land_by_season, name='get-land-by-season'),
    path('api/get-land-info/<int:land_id>/', views.get_land_info, name='get-land-info'),
    path('api/get-plant-by-land/<int:land_id>/', views.get_plant_by_land, name='get-plant-by-land'),
<<<<<<< HEAD
=======


    path('marker/', views.marker2, name="marker"),
    path('maker/sell', views.get_maker_sell, name="maker_sell"),    
    path('search/', views.search, name='search'),

    path('contact/', views.contact, name="contact"),
   
>>>>>>> 83649d5c415e276eb467f4fc3808f4d13b3cf561
]

# Tạo một danh sách mới chỉ chứa urlpatterns cho đường dẫn 'search'
search_urlpatterns = [
    path('search', views.search, name='search'),
]

# Kết hợp static settings chỉ cho search_urlpatterns
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
