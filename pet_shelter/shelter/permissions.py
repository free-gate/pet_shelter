from rest_framework.permissions import BasePermission


class AccessPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            return request.user.has_perm('shelter.view_pet')
        elif request.method == "POST":
            return request.user.has_perm('shelter.add_pet')
        elif request.method in ["PUT", "PATCH"]:
            return request.user.has_perm('shelter.change_pet')
        elif request.method == "DELETE":
            return request.user.has_perm('shelter.delete_pet')
        return True

    def has_permission(self, request, view):
        if request.method == "GET":
            return request.user.has_perm('shelter.view_pet')
        elif request.method == "POST":
            return request.user.has_perm('shelter.add_pet')
        elif request.method in ["PUT", "PATCH"]:
            return request.user.has_perm('shelter.change_pet')
        elif request.method == "DELETE":
            return request.user.has_perm('shelter.delete_pet')
        return True
