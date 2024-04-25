from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    """"""
    def create_user(self, phone_number, password=None, **other_fields):
        if not phone_number:
            raise ValueError('User must have phone number...!')

        # check favorite fields ...!

        user = self.model(
            phone_number=phone_number,
            # you can give to user model your favorite fields...!
            **other_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')

        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')

        user = self.create_user(phone_number, password, **other_fields)
        user.save(using=self._db)
        return user
