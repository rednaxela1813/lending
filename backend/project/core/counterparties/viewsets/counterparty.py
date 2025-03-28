from rest_framework import viewsets, permissions
from core.counterparties.models import Counterparty
from core.counterparties.serializers import CounterpartySerializer


class CounterpartyViewSet(viewsets.ModelViewSet):
    serializer_class = CounterpartySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Counterparty.objects.filter(owner=self.request.user).order_by('-created')
    

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    

