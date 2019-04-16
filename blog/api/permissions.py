from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
	my_safe_method = ['GET', 'PUT', 'DELETE']
	def has_permission(self, request, view):
		if request.method in self.my_safe_method:
			return True
		return False


	def has_object_permission(self, request, view, obj):
		if request.method in SAFE_METHODS:
			return True
		return obj.posted_by == request.user