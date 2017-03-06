from django.conf.urls import url, include
from django.contrib import admin
from api.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'payment_types', PaymentTypeViewSet)
router.register(r'product_types', ProductTypeViewSet)
router.register(r'user', UserViewSet)
router.register(r'line_items', LineItemViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]