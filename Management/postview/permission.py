from rest_framework import permissions
from .models import Note_User

class ModifyNotePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in ('PUT', 'DELETE'):
            try:
                pk = view.kwargs.get('pk')
            except:
                pass
            user = request.user
            try:
                note = Note_User.objects.get(pk=pk)
                if note.user == user:
                    return True
                else:
                    return False
            except Note_User.DoesNotExist:
                return False
        return True
