from rest_framework.filters import BaseFilterBackend
from rest_framework.exceptions import APIException


class BelongToOwner(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        return queryset.filter(owner=request.user)
