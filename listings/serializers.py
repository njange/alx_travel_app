from rest_framework import serializers
from .models import Listing, ListingImage

class ListingImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingImage
        fields = ['id', 'image', 'caption', 'is_primary', 'created_at']

class ListingSerializer(serializers.ModelSerializer):
    images = ListingImageSerializer(many=True, read_only=True)
    owner_name = serializers.CharField(source='owner.username', read_only=True)
    
    class Meta:
        model = Listing
        fields = [
            'id', 'title', 'description', 'listing_type', 'price_per_night',
            'location', 'address', 'latitude', 'longitude', 'max_guests',
            'bedrooms', 'bathrooms', 'amenities', 'is_active', 'owner',
            'owner_name', 'images', 'created_at', 'updated_at'
        ]
        read_only_fields = ['owner', 'created_at', 'updated_at']
    
    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)

class ListingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = [
            'title', 'description', 'listing_type', 'price_per_night',
            'location', 'address', 'latitude', 'longitude', 'max_guests',
            'bedrooms', 'bathrooms', 'amenities', 'is_active'
        ]
    
    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)

class ListingUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = [
            'title', 'description', 'listing_type', 'price_per_night',
            'location', 'address', 'latitude', 'longitude', 'max_guests',
            'bedrooms', 'bathrooms', 'amenities', 'is_active'
        ]
