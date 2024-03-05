from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter() # Router

router.register('list', views.ProductViewset) # router er antenna
router.register('size', views.SizeViewset) # router er antenna
router.register('category', views.CategoryViewset) # router er antenna
router.register('color', views.ColorViewset) # router er antenna
router.register('reviews', views.ReviewViewset) # router er antenna


urlpatterns = [
    path('', include(router.urls)),
]