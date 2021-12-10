from django.conf.urls import include, url
from rest_framework import routers

from .views import ProdutoViewSet

router = routers.DefaultRouter()
router.register(r'produtos', ProdutoViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
