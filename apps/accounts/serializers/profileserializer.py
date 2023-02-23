from rest_framework.serializers import ModelSerializer

from apps.core.models import Profile

class ProfileModelSerializer(ModelSerializer):
    
    class Meta:
        model = Profile
        fields = (
            'picture',
        )
    
