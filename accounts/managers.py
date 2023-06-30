from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """
    Custom manager for the custom NewUser model below
    """

    def create_superuser(self, email, password,
                         **other_fields):
        # Set is_staff, is_superuser, and is_active to True as default
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        return self.create_user(email=email,
                                password=password,
                                **other_fields)

    def create_user(self, email, full_name, password=None,
                    **other_fields):
        # Set the values to the variables for creating a user account
        email = self.normalize_email(email)
        user = self.model(full_name=full_name,
                          email=email,
                          **other_fields)
        user.set_password(password)
        user.save()
        return user
