from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """ ensure user edits only their own profile"""
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id
    
    
class UpdateOwnFeedItem(permissions.BasePermission):
    """ ensure user edits only their own feed ote,"""
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user_profile_id == request.user.id