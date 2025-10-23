from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # Muestra estos campos en la lista de perfiles
    list_display = ('name', 'title', 'slug', 'is_active')
    
    # Añade un campo de búsqueda
    search_fields = ('name', 'title', 'slug')
    
    # Pre-llena el slug basado en el nombre (muy útil)
    prepopulated_fields = {'slug': ('name',)}