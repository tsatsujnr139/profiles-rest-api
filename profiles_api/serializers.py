from rest_framework import serializers
from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """serializers a name field for an apiview"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """ validates a user profile object """

    class Meta:
        model = models.UserProfile
        fields = '__all__'
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }
            }
        }

    def create(self, validated_data):
        """creates a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """ validates a profile feed item """

    class Meta:
            model = models.ProfileFeedItem
            fields = '__all__'
            extra_kwargs = {
            'user_profile': {
                'read_only': True
            }
        }
