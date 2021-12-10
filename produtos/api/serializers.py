from rest_framework import serializers

from produtos.api.models import Produto


class ProdutoSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Produto
        fields = (
            'id', 'owner', 'created_datetime', 'title',
            'content', 'price'
        )
        read_only_fields = (
            'id', 'created_datetime'
        )

    def to_representation(self, instance):
        data = super(ProdutoSerializer, self).to_representation(instance=instance)
        data['owner'] = instance.owner.username
        return data
