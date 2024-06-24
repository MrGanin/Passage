import django_filters
from rest_framework import viewsets
from .serializers import *
from .models import *



class PassageAPIView(viewsets.ModelViewSet):
   queryset = Passage.objects.all()
   serializer_class = PassageSerializer
   filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
   filterset_fields = ['user__email']

# Create your views here.
