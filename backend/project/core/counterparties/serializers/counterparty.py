from rest_framework import serializers
from core.counterparties.models import Counterparty


class CounterpartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Counterparty
        fields = '__all__'
        read_only_fields = ('public_id', 'owner', 'created', 'updated')
