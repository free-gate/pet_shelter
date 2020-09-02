from rest_framework.permissions import BasePermission


class AccessPermission(BasePermission):

    def _check_request(self, request):
        perm = False
        if request.method == "GET":
            perm = request.user.has_perm('shelter.view_pet')
        elif request.method == "POST":
            perm = request.user.has_perm('shelter.add_pet')
        elif request.method in ["PUT", "PATCH"]:
            perm = request.user.has_perm('shelter.change_pet')
        elif request.method == "DELETE":
            perm = request.user.has_perm('shelter.delete_pet')
        return perm

    def has_object_permission(self, request, view, obj):
        return self._check_request(request)

    def has_permission(self, request, view):
        return self._check_request(request)
