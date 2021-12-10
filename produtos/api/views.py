from rest_framework import viewsets
from rest_framework.filters import OrderingFilter

from url_filter.filtersets import ModelFilterSet
from url_filter.integrations.drf import DjangoFilterBackend

from produtos.api.models import Produto
from produtos.api.serializers import ProdutoSerializer

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope, OAuth2Authentication
from rest_framework.authentication import SessionAuthentication

from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from .filters import BelongToOwner


class ProdutoFilter(ModelFilterSet):
    class Meta:
        model = Produto


@method_decorator(name='create', decorator=swagger_auto_schema(
    operation_summary="Criar um novo Produto",
    operation_description="Endpoint para criar um novo produto",
))
@method_decorator(name='destroy', decorator=swagger_auto_schema(
    operation_summary="Deletar um produto",
    operation_description="Endpoint para deletar um produto",
))
@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_summary="Listar os produtos cadastradas",
    operation_description="Endpoint para listar os produtos cadastradas",
))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(
    operation_summary="Listar um produto",
    operation_description="Endpoint para listar um produto",
))
@method_decorator(name='update', decorator=swagger_auto_schema(
    operation_summary="Atualizar um produto",
    operation_description="Endpoint para atualizar um produto",
))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(
    operation_summary="Editar um produto parcial",
    operation_description="Endpoint para Editar um produto parcial",
))
class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all().order_by('-id')
    serializer_class = ProdutoSerializer
    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [TokenHasReadWriteScope]
    filter_backends = [DjangoFilterBackend, OrderingFilter, BelongToOwner]
    filter_class = ProdutoFilter

