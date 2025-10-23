from django.urls import path
from .views import ProfileDetailView

urlpatterns = [
    # Esta es la URL: api/profiles/<slug-del-perfil>/
    path('<slug:slug>/', ProfileDetailView.as_view(), name='profile-detail'),
]