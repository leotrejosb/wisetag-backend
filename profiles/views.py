from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer

class ProfileDetailView(generics.RetrieveAPIView):
    """
    Vista de API para obtener un solo perfil por su 'slug'.
    """
    queryset = Profile.objects.filter(is_active=True) # Solo muestra perfiles activos
    serializer_class = ProfileSerializer
    lookup_field = 'slug' # Le dice a DRF que busque por el campo 'slug'
