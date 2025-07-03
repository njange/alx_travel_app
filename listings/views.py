from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Listing, ListingImage
from .serializers import (
    ListingSerializer, 
    ListingCreateSerializer,
    ListingUpdateSerializer
)

class ListingViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing listing instances.
    """
    queryset = Listing.objects.filter(is_active=True)
    serializer_class = ListingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_serializer_class(self):
        if self.action == 'create':
            return ListingCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return ListingUpdateSerializer
        return ListingSerializer
    
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return [permission() for permission in permission_classes]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        queryset = Listing.objects.filter(is_active=True)
        
        # Filter by location
        location = self.request.query_params.get('location')
        if location:
            queryset = queryset.filter(
                Q(location__icontains=location) | 
                Q(address__icontains=location)
            )
        
        # Filter by listing type
        listing_type = self.request.query_params.get('type')
        if listing_type:
            queryset = queryset.filter(listing_type=listing_type)
        
        # Filter by price range
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')
        if min_price:
            queryset = queryset.filter(price_per_night__gte=min_price)
        if max_price:
            queryset = queryset.filter(price_per_night__lte=max_price)
        
        # Filter by guests
        guests = self.request.query_params.get('guests')
        if guests:
            queryset = queryset.filter(max_guests__gte=guests)
        
        return queryset
    
    @swagger_auto_schema(
        method='get',
        manual_parameters=[
            openapi.Parameter('location', openapi.IN_QUERY, description="Filter by location", type=openapi.TYPE_STRING),
            openapi.Parameter('type', openapi.IN_QUERY, description="Filter by listing type", type=openapi.TYPE_STRING),
            openapi.Parameter('min_price', openapi.IN_QUERY, description="Minimum price per night", type=openapi.TYPE_NUMBER),
            openapi.Parameter('max_price', openapi.IN_QUERY, description="Maximum price per night", type=openapi.TYPE_NUMBER),
            openapi.Parameter('guests', openapi.IN_QUERY, description="Minimum number of guests", type=openapi.TYPE_INTEGER),
        ],
        responses={200: ListingSerializer(many=True)}
    )
    @action(detail=False, methods=['get'])
    def search(self, request):
        """
        Search listings with filters
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def my_listings(self, request):
        """
        Get current user's listings
        """
        queryset = Listing.objects.filter(owner=request.user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
