from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, phone, password=None):
        """
        Creates and saves a User with the given phone number and password.
        """
        if not phone:
            raise ValueError('Users must have an phone number')

        # Saves the user
        user = self.model(
            phone=self.normalize_email(phone),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None):
        """
        Creates and saves a superuser with the given phone number and password.
        """
        user = self.create_user(
            phone,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
