from rest_framework.permissions import BasePermission


class IsActive(BasePermission):
    """
    Пермишен для проверки активности пользователя. Разрешает доступ только активным пользователям.
    """

    def has_permission(self, request, view):
        # Проверяет, является ли пользователь аутентифицированным и активным.
        return request.user.is_authenticated and request.user.is_active


class IsOwner(BasePermission):
    """
    Пермишен для проверки владельца объекта. Разрешает доступ только владельцу объекта.
    """
    message = "Вы не являетесь владельцем!"

    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
        return False
