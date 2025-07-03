from django.contrib import admin
from .models import Listing, ListingImage

class ListingImageInline(admin.TabularInline):
    model = ListingImage
    extra = 1
    readonly_fields = ['created_at']

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ['title', 'listing_type', 'location', 'price_per_night', 'owner', 'is_active', 'created_at']
    list_filter = ['listing_type', 'is_active', 'created_at', 'location']
    search_fields = ['title', 'location', 'address', 'description']
    readonly_fields = ['created_at', 'updated_at']
    inlines = [ListingImageInline]
    
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'listing_type', 'owner', 'is_active')
        }),
        ('Location', {
            'fields': ('location', 'address', 'latitude', 'longitude')
        }),
        ('Property Details', {
            'fields': ('price_per_night', 'max_guests', 'bedrooms', 'bathrooms', 'amenities')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(ListingImage)
class ListingImageAdmin(admin.ModelAdmin):
    list_display = ['listing', 'caption', 'is_primary', 'created_at']
    list_filter = ['is_primary', 'created_at']
    search_fields = ['listing__title', 'caption']
    readonly_fields = ['created_at']
