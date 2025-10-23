from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        # Estos son los campos que tu API va a mostrar
        fields = [
            'name', 'slug', 'title', 'bio', 'profile_picture_url', 
            'whatsapp_number', 'instagram_username', 'linkedin_url', 
            'email', 'website_url', 'is_active'
        ]
