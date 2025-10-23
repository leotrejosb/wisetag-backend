from django.contrib import admin
from django.urls import path, include  # <-- 1. Asegúrate de importar 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # --- 2. AÑADE ESTA LÍNEA ---
    # Esto le dice a Django: "Oye, cualquier URL que empiece con 'api/profiles/'
    # envíasela a la app 'profiles' para que ella decida qué hacer."
    path('api/profiles/', include('profiles.urls')),
]