from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    
    # El 'slug' es la URL única, ej: "carlos-perez"
    slug = models.SlugField(max_length=100, unique=True, verbose_name="Slug (URL)")
    
    title = models.CharField(max_length=100, verbose_name="Título", help_text="Ej: Abogado de Familia")
    bio = models.TextField(verbose_name="Biografía", blank=True)
    
    # Usamos URLField para los links. blank=True significa que son opcionales.
    profile_picture_url = models.URLField(verbose_name="URL Foto de Perfil", blank=True)
    whatsapp_number = models.CharField(max_length=20, verbose_name="Número WhatsApp", blank=True, help_text="Ej: 573001234567")
    instagram_username = models.CharField(max_length=50, verbose_name="Usuario Instagram", blank=True, help_text="Solo el usuario, sin @")
    linkedin_url = models.URLField(verbose_name="URL de LinkedIn", blank=True)
    email = models.EmailField(verbose_name="Email de Contacto", blank=True)
    website_url = models.URLField(verbose_name="URL Sitio Web", blank=True)
    
    # Campo para saber si el perfil está activo
    is_active = models.BooleanField(default=True, verbose_name="Perfil Activo")

    def __str__(self):
        # Esto es para que se vea bonito en el Admin de Django
        return self.name