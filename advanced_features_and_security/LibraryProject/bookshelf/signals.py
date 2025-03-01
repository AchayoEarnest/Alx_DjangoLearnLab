from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group, Permission
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from .models import Book

@receiver(post_migrate)
def create_groups_and_permissions(sender, **kwargs):
    if sender.name == "bookshelf":
        content_type = ContentType.objects.get_for_model(Book)

        permissions = {
            "can_view": "Can view book details",
            "can_create": "Can add new book",
            "can_edit": "Can edit book details",
            "can_delete": "Can delete book",
        }

        for codename, name in permissions.items():
            perm, created = Permission.objects.get_or_create(codename=codename, name=name, content_type=content_type)

        groups_permissions = {
            "Viewers": ["can_view"],
            "Editors": ["can_view", "can_edit", "can_create"],
            "Admins": ["can_view", "can_edit", "can_create", "can_delete"],
        }

        for group_name, perms in groups_permissions.items():
            group, created = Group.objects.get_or_create(name=group_name)
            group.permissions.set(Permission.objects.filter(codename__in=perms))
